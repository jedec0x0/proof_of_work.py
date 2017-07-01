import hashlib
import time
import itertools

range = lambda stop: iter(itertools.count().next, stop)
max_nonce = 2 ** 32

def proof_of_work(header, difficulty_bits):
    target = 2 ** (256-difficulty_bits)
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()
        if long(hash_result, 16) < target:
            print "[+]Success with nonce %d" % nonce
            print "[+]Hash is %s" % hash_result
            return (hash_result,nonce)
    print "[-]Failed after %d (max_nonce) tries" % nonce
    return nonce

def main():
    nonce = 0
    hash_result = 'blah'
    for difficulty_bits in xrange(32):
        difficulty = 2 ** difficulty_bits
        print "[*] Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits)
        print "[*]Starting search..."
        start_time = time.time()
        new_block = 'just a bogus string' + hash_result
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print "[*]Elapsed Time: %.4f seconds" % elapsed_time
        if elapsed_time > 0:
            hash_power = float(long(nonce)/elapsed_time)
            print "[*]Hashing Power: %d hashes per second" % hash_power

if __name__ == "__main__":
    main()
