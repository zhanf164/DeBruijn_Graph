#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:48:06 2020

@author: zach
"""


from graphviz import Digraph


class DeBruijnGraph():
    
    def __init__(self, reads, klength):
        self.nodes = []
        self.edges = {}
        self.kmers = self.Generate_Kmers(reads, klength)
        self.rights, self.lefts = self.AddtoGraph(self.kmers)
        self.isEulerian = self.CheckifEulerian(self.rights, self.lefts)
    
    def Generate_Kmers(self, reads, klength):
        kmers = []
        for read in reads:
            for i in range((len(read)-klength)+1):
                kmers.append(read[i:i+klength])
                
        return kmers    


    def AddtoGraph(self, kmers):
        lefts = set()
        rights = set()
        for kmer in kmers:
            leftmer = kmer[:-1]
            rightmer = kmer[1:]
            if leftmer in self.nodes:
                pass
            else:
                self.nodes.append(leftmer)
            if rightmer in self.nodes:
                pass
            else:
                self.nodes.append(rightmer)
            if leftmer in self.edges:
                if rightmer in self.edges[leftmer][0]:
                    ind_rightmer = self.edges[leftmer][0].index(rightmer)
                    self.edges[leftmer][1][ind_rightmer] = self.edges[leftmer][1][ind_rightmer] + 1
                else:
                    self.edges[leftmer][0].append(rightmer)
                    self.edges[leftmer][1].append(1)
            else:
                self.edges[leftmer] = [[rightmer], [1]]
            rights.add(rightmer)
            lefts.add(leftmer)
        return rights, lefts
        
    def CheckifEulerian(self, rights, lefts):
        if len(rights ^ lefts) == 2:
            return True
        return False
        
        
    def WalkGraph(self, edges, nodes):
        pass
        
    def DrawGraph(self):
        dot = Digraph()
        for key, value in self.edges.items():
            for edg, weight in zip(value[0], value[1]):
                dot.edge(key, edg, label=str(weight))
        for node in self.nodes:
            dot.node(node)
    
        dot.render(view=True)
        
    