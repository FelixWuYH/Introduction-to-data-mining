
if (!require(arules)) {
  install.packages("arules")
  library(arules)
} 
if (!require(arulesViz)) {
  install.packages("arulesViz")
  library(arulesViz)
} 
########
data<-read.csv(file = "活頁簿1.csv")
data$Tid<-NULL
trans <- as(data, "transactions")
rule <- apriori(trans, 
                parameter=list(minlen=2, supp=0.1, conf=0.1),  
                appearance = list(default="lhs",
                                  rhs=c("Cheat=Yes","Cheat=No")
                )          
)

inspect(rule)
sortconf<-sort(rule, by="conf")
inspect(sortconf)
