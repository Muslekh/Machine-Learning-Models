crime <- read.csv(file.choose())

# Normalizing continuous columns to bring them under same scale
normalized_data<-scale(crime[,2:5]) #excluding the X name column before normalizing
View(normalized_data)
wss = NULL

twss <- NULL
for (i in 2:15){
  twss <- c(twss,kmeans(normalized_data,i)$tot.withinss)
  
}

plot(2:15, twss,type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")   # Look for an "elbow" in the scree plot #
title(sub = "K-Means Clustering Scree-Plot")
k_3 <- kmeans(normalized_data,3)
str(k_3)
clust=k_3$cluster
final=data.frame(crime,clust)
aggregate(crime[,-1],by=list(final$clust),mean)
