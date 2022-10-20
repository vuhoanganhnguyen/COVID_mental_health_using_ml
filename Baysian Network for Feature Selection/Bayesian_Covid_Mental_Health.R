library("readr")
library("tidyverse")

setwd("E:\\Study\\TRU\\Third Year\\Winter 2022\\COMP 3710 Applied Artificial Intelligence\\Project\\Data\\Baysian Network for Feature Selection")
data <- read.table("Dataset_after_Bayesian_MXM.csv", sep= ",",
                   header=TRUE, stringsAsFactors = TRUE)
summary(data)
# this loads the data
                             # Install & load dplyr package
library("dplyr")

library("bnlearn")
# this loads the bnlearn package
library("qgraph")
# this loads the qgraph package

t <- data.frame(matrix(as.numeric(unlist(data)),ncol = length(data[1,])))
rownames(t) <- rownames(data)
colnames(t) <- colnames(data)
data <- t

BNpc <- hc(data)
# this performs the algorithm
qgraph(BNpc)
# this plots the network

BST <- boot.strength(data,
                     # this includes data
                     R = 200,
                     # number of boots
                     algorithm = "hc")
bst1 <- BST[BST$strength > 0.85 & BST$direction > 0.5, ]
# this sets the minimum direction
avgnet1 <- averaged.network(BST, threshold = 0.85)
# compute the average network
qgraph(avgnet1, layout="circle")
# this plots the network with qgraph