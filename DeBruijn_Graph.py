#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:48:06 2020

@author: zach
"""



class DeBruijnGraph():
    
    def __init__(self, reads):
        self.nodes = []
        self.edges = {}
        
    
    
    def Generate_Kmers(self, reads, klength):
        kmers = []
        for read in reads:
            for i in range(len(read)-klength):
                kmers.append(read[i:i+klength])
                
        return kmers    
    
    def AddtoGraph(self, kmers):
        for kmer in kmers:
            leftmer = kmer[:-1]
            rightmer = kmer[1:]
            if leftmer in self.nodes:
                pass
            else:
                self.nodes.append(leftmer)
            if rightmer in self.nodes:
                passsfo
            else:
                self.nodes.append(rightmer)
            if leftmer in self.edges():
                self.edges[leftmer].append(rightmer)
            else:
                self.edges[leftmer] = [rightmer]
        
    
    def EulerianWalk(self, nodes, edges):
        pass