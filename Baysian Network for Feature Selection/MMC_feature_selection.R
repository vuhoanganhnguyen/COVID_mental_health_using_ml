library(MXM)
setwd("E:\\Study\\TRU\\Third Year\\Winter 2022\\COMP 3710 Applied Artificial Intelligence\\Project\\Data\\Baysian Network for Feature Selection")
data <- read.table("Dataset_after_Chi_square.csv", sep= ",",
                   header=TRUE, stringsAsFactors = TRUE)

t <- data.frame(matrix(as.numeric(unlist(data)),ncol = length(data[1,])))
rownames(t) <- rownames(data)
colnames(t) <- colnames(data)
data <- t

str(data)

targetVariable <- data$MH_05
targetVariable <- NULL

covid_dataset <- as.matrix(data[, -1])
covid_dataset[, 10] <- as.numeric(covid_dataset[, 10])
head(covid_dataset, 2)

dim(covid_dataset)

target_Mental <- as.vector(data$MH_05)
str(target_Mental,2)

mmpcobject_data_Mental <- MXM::MMPC( target  = target_Mental,            
                                      dataset = covid_dataset,            
                                      max_k = 3,          
                                      threshold = 0.05,                                         
                                      test = 'testIndFisher',   
                                      ini = NULL,                                                
                                      hash =  TRUE,      
                                      hashObject = NULL,                                        
                                      ncores = 1,         
                                      backward = TRUE)   

summary(mmpcobject_data_Mental)

mmpcobject_data_Mental@selectedVarsOrder

colnames(covid_dataset)[14]
