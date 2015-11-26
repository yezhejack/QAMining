#coding:utf-8
#! /usr/bin/env python

from collections import defaultdict

#db= [
#    ['a','b','c','d','e'],
#    ['b','b','b','d','e'],
#    ['c','b','c','c','a'],
#    ['b','b','b','c','c'],
#]

def prefixspan(db,minsup):
    results = []

    def mine_rec(patt, mdb):
        def localOccurs(mdb):
            occurs = defaultdict(list)

            for (i, stoppos) in mdb:
                seq = db[i]
                for j in xrange(stoppos, len(seq)):
                    l = occurs[seq[j]]
                    if len(l) == 0 or l[-1][0] != i:
                        l.append((i, j + 1))

            return occurs

        for (c, newmdb) in localOccurs(mdb).items():
            newsup = len(newmdb)

            if newsup >= minsup:
                newpatt = patt + [c]

                results.append((newpatt, [i for (i, stoppos) in newmdb]))
                mine_rec(newpatt, newmdb)

    mine_rec([], [(i, 0) for i in xrange(len(db))])

    print(results)
