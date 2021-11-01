### Loading Packages
##```{r preparation-load-packages, message = FALSE, warning = FALSE}
# load necessary library and packages for the analysis
library(dplyr) 
library(tidyr)
library(readxl)
library(RColorBrewer)

library(ggplot2)
library(table1)
library(arsenal)
library(gtsummary)
library(corrplot)
library(rcompanion)
library(knitr)
library(rpivotTable)
library(flexdashboard)
library(DT)
library(car) 
library(rms)
library(leaps)
library(psych)
library(pca3d)
library(animation)
library(gt)
library(nortest)
library(DT)
library(sandwich)
library(lmtest)
library(wooldridge)
library(table1)
library(arsenal)
library(gtsummary)
library(gt)
library(corrplot)
library(xtable)
library(rcompanion)
library(car)
library(rstatix)

#library(factoexrta)
library(caret) # install 'caret' package with 'dependencies=TRUE' turned on
library(AER)   
library(plm)    
library(stargazer)      
library(lattice)
library(ivreg) # IV-regression

getwd()
# change to desired working directory with all relevant files 
setwd("C:/Users/User/Desktop")
anova_test_sad = read.csv(file = 'ANOVA_test_sad.csv', header = TRUE)
head(anova_test_sad)

class(anova_test_sad)# check if data frame else conver to data.table


library(data.table) # for converting data frame to data.table object

setDT(anova_test_sad) # this is to convert anova_test_sad data frame to a data table

df_long <- melt(data = anova_test_sad, 
                id.vars = c("pMail"),
                variable.name = "Questions",
                value.name = "Sad_Ratings")
 df_long
 
 write.table(df_long, "anova_testsad_long.csv", row.names=FALSE, sep=",")

#computing some summary statisitcs of sad_ratings by point_in_time(questions)
 
 df_long %>%
   group_by(Questions) %>%
   get_summary_stats(Sad_Ratings, type = "mean_sd")
 
 install.packages("ggplot2")
 install.packages("ggpubr")
 library(ggpubr)
 library(tidyverse)
 
 bxp <- ggboxplot(df_long, x = "Questions", y = "Sad_Ratings", add = "point", color = "Questions", palette =c("#00AFBB", "#E7B800", "#FC4E07","#FC4E07"))
 bxp
 
 p1 <- ggpar(bxp, 
             title = "Mean of participants sad ratings across 3 audio clips",
             caption = "Source: ggpubr",
             xlab ="Questions To Elicit Sad Emotions From Pre & Post Listening", 
             ylab = "Sad Ratings",
             legend.title = "Questions (Ratings Scale)")
 p1 
 
 
 #----------------------------------------------------------------------------
 
 anova_test_happy = read.csv(file = 'ANOVA_test_happy.csv', header = TRUE)
 head(anova_test_happy)
 
 class(anova_test_happy)# check if data frame else convert to data.table
 
 setDT(anova_test_happy) # this is to convert anova_test_sad data frame to a data table
 
 df_long_2 <- melt(data = anova_test_happy, 
                 id.vars = c("pMail"),
                 variable.name = "Questions",
                 value.name = "Happy_Ratings")
 df_long_2
 
 write.table(df_long_2, "anova_happy_long.csv", row.names=FALSE, sep=",")
 
 df_long_2 %>%
   group_by(Questions) %>%
   get_summary_stats(Happy_Ratings, type = "mean_sd")
 
 bxp2 <- ggboxplot(df_long_2, x = "Questions", y = "Happy_Ratings", add = "point", color = "Questions", palette =c("#00AFBB", "#E7B800", "#FC4E07","#FC4E07"))
 bxp2
 
 p2 <- ggpar(bxp2, 
             title = "Mean of participants happy ratings across 3 audio clips",
             caption = "Source: ggpubr",
             xlab ="Questions To Elicit Happy Emotions From Pre & Post Listening", 
             ylab = "Happy Ratings",
             legend.title = "Questions (Ratings Scale)")
 p2 
 
 
 
