crime <- read.csv(file.choose())

# Normalizing continuous columns to bring them under same scale
normalized_data<-scale(crime[,2:5]) 
?dist
d <- dist(normalized_data, method = "euclidean") # distance matrix
?hclust
fit <- hclust(d, method="complete")
?hclust
plot(fit) # display dendrogram
plot(fit, hang=-1)

?cutree
rect.hclust(fit, k=3, border="red")
?rect.hclust
groups <- cutree(fit, k=4) # cut tree into 4 clusters

clust<-as.matrix(groups) # groups or cluster numbers
final <- data.frame(crime, clust)

View(final)

write.csv(final, file="final.csv",row.names = F)

aggregate(crime[,-1],by=list(final$clust),mean)
