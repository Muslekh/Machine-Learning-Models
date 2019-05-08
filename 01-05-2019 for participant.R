library(readr)

c1 <- read.csv(file.choose())

View(c1)

str(c1)  #to know structure of data
table(c1$Type)  #to know count of classifiers

#table or proportions with informative labels
round(prop.table(table(c1$Type))*100,digits = 1)

c1$Type=as.factor(c1$Type)
#create stardadization function
normalize <- function(x){
  return((x-min(x)) / (max(x) - min(x)))
}

#normalize the data
c1_n <- as.data.frame(lapply(c1[1:9],normalize))

glass_data <- sample(1:nrow(c1),size=nrow(c1)*0.7,replace = FALSE)

c1_train <- c1_n[glass_data,] # 70% training data
c1_test <- c1_n[-glass_data,]

#divide the test and train data
c1_train_labels <- c1[glass_data,10]
c1_test_labels  <- c1[-glass_data,10] 


#install.packages(class)
library(class)
NROW(c1_train_labels)
knn.26 <-  knn(train=c1_train, test=c1_test, cl=c1_train_labels, k=10)
ACC.26 <- 100 * sum(c1_test_labels == knn.26)/NROW(c1_test_labels)
mean(knn.26==c1_test_labels)
ACC.26

knn.27 <-  knn(train=c1_train, test=c1_test, cl=c1_train_labels, k=11)
ACC.27 <- 100 * sum(c1_test_labels == knn.27)/NROW(c1_test_labels)  
ACC.27
