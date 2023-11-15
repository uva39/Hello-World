library(wordcloud)
setwd("/Users/uva/Downloads")

TEXT <- scan(file = "08_Sejong_UTF-8.txt", what = "character", quote = NULL, sep="\n", encoding = "UTF-8") # nolint


a <- grep("^9BT", TEXT, value = TRUE)
b <- unlist(strsplit(a, "\t"))
c <- b[seq(3, length(b), by = 3)]
Mors <- unlist(strsplit(c, " [+] "))