import os, sys, hashlib
#import RBTree

import zlib


class deduplicator:
    def __init__(self):
        self.hashs = {}
        self.offsets = {}
        self.block_size =  4096
        self.file_offset = 0
        self.nb_dedup_carac = 0
        #zlib.compress(
        self.nb_dedup_carac_compressed = 0

    #for f in files:
    def deduplicate_file_variable(self, f):
        print "Open", f
        fd = open(f)

        i = 0
        #file_offset = 0

        offset = 0
        buf = ''

        nb_uncache_carac = 0
        #nb_dedup_carac = 0
        nb_dedup_saves = 0

        while True:
            #print "I:", i
            i += 1

            #print "New loop", offset


            #print "Global offset :", file_offset
            prior = len(buf)

            buf = buf + fd.read(self.block_size * 2 - offset)

            after = len(buf)
            nb_add_caracters = after - prior
            #print "We read", nb_add_caracters
            self.file_offset += nb_add_caracters

            if len(buf) == 0:
                #print "New file"
                break

            #print "Len hashs", len(hashs), "Len buf", len(buf)
            #print "Buf :", buf
            still_loop = True
            j = 0
            initial_hash = None
            initial_string = None
            while True:
                #print "Len buf", len(buf)
                part = buf[self.block_size - offset : self.block_size * 2 -offset]
                #print "Part", part
                #print "Part (len:%d)" % len(part), "From" ,block_size - offset, " to", block_size * 2 - offset

                #print "Part :", len(part)
                m = hashlib.md5()
                m.update(part)

                hash = m.hexdigest()            
                if j == 0:
                    #print "Initial", len(part), block_size - offset, -offset
                    initial_hash = hash
                    initial_string = part
                    #print "Initial string", initial_string, "END"
                    #print "Part", part, "END"
                j += 1


                if hash in self.hashs:
                    still_loop = False
                    #if offset != 0 and offset != self.block_size:
                        #print "Find a matching hash!", offset
                        #print "Reference (%s)@(%d):" % (hash, offsets[hash]) ,":", hashs[hash]
                        #print "Match (%s):@(%d)" % (hash, file_offset - offset), ":", part

                    self.nb_dedup_carac += len(part)
                    self.nb_dedup_carac_compressed += 2* len(part) - len(zlib.compress(part))
                    nb_dedup_saves += 1

                    #m = hashlib.sha1()
                    part1 = buf[:self.block_size * 2 - offset]
                    m1 = hashlib.md5()
                    m1.update(part1)
                    hash_part1 = m1.hexdigest()
                    if hash_part1 not in self.hashs:
                        self.hashs[hash_part1] = part1
                        self.offsets[hash_part1] = self.file_offset - nb_add_caracters
                        nb_uncache_carac += len(part1)
                    else:
                        self.nb_dedup_carac += len(part1)
                        self.nb_dedup_carac_compressed += 2* len(part1) - len(zlib.compress(part1))
                        nb_dedup_saves += 1

                    buf = buf[self.block_size * 2 - offset:]

                    #print "Good break at j:",j-1
                    j = 0
                    break

                if offset == self.block_size:
                    offset = 0
                    buf = ''
                    self.hashs[hash] =  part
                    self.offsets[hash] = self.file_offset - self.block_size * 2
                    nb_uncache_carac += len(part)

                    self.hashs[initial_hash] = initial_string 
                    self.offsets[initial_hash] = self.file_offset - self.block_size
                    nb_uncache_carac += len(initial_string)

                    #print "Not find..."
                    still_loop = False

                    #print "Bad break at j:",j-1
                    j = 0
                    break

                offset += 1

        print "Global offset", self.file_offset
        #print c, m.hexdigest()
        print self.file_offset - nb_uncache_carac
        print "Overall: Undedup:%d Dedup:%d Dedup+compressed:%d" % (nb_uncache_carac, self.nb_dedup_carac, self.nb_dedup_carac_compressed)
        print "Total bloc saves", nb_dedup_saves
      


    #for f in files:
    def deduplicate_file_fix(self, f):
        print "Open", f
        fd = open(f)

        i = 0
        offset = 0
        buf = ''

        nb_uncache_carac = 0
        #nb_dedup_carac = 0
        nb_dedup_saves = 0

        while True:
            #print "I:", i
            i += 1
            
            
            buf = fd.read(self.block_size)
            self.file_offset += len(buf)
            
            if len(buf) == 0:
                break

            m = hashlib.md5()
            m.update(buf)

            hash = m.hexdigest()            
            
            if hash in self.hashs:
                #print "Find a matching hash!"
                #print "Reference (%s)@(%d):" % (hash, offsets[hash]) ,":", hashs[hash]
                #print "Match (%s):@(%d)" % (hash, file_offset - offset), ":", part

                self.nb_dedup_carac += len(buf)
                self.nb_dedup_carac_compressed += 2 * len(buf) - len(zlib.compress(buf))
                nb_dedup_saves += 1

            else:
                self.hashs[hash] =  None#buf
                nb_uncache_carac += len(buf)

        #print "Global offset", self.file_offset
        #print "Overall: Dedup:%d" % self.nb_dedup_carac
        print "Total bloc saves", nb_dedup_saves



d = deduplicator()
f = deduplicator()
for root, dirs, files in os.walk(sys.argv[1]):
    for fd in files:
        d.deduplicate_file_variable(root+'/'+fd)
        print "****** Stats Varible: Deplicated %d/%d = %.2f%% Dedup+compress %d =%.2f%%" % (d.nb_dedup_carac,d.file_offset, d.nb_dedup_carac*100/d.file_offset, d.nb_dedup_carac_compressed, d.nb_dedup_carac_compressed*100/d.file_offset)

        f.deduplicate_file_fix(root+'/'+fd)
        print "****** Stats Fix: Deplicated %d/%d = %.2f%% Dedup+compress %d =%.2f%%" % (f.nb_dedup_carac,f.file_offset, f.nb_dedup_carac*100/f.file_offset, f.nb_dedup_carac_compressed, f.nb_dedup_carac_compressed*100/f.file_offset)


        
        #print "Root", root
    #print "Dirs", dirs
    #print "Files", files



