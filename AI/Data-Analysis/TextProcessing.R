library(wordcloud)

TEXT <- scan(file = "07_data01.txt", what = "character", quote = NULL)
TEXT <- iconv(TEXT, from = "iso-8859-1", to = "UTF-8")

TEXT <- gsub("^[[:punct:]]+|[[:punct:]]+$", "", TEXT)
TEXT <- tolower(TEXT)

bi.grams <- paste(TEXT[1:length(TEXT)-1], TEXT[2:length(TEXT)], sep=" ")
bi.grams <- table(bi.grams)
bi.grams <- data.frame(bi.grams)

wordcloud(
    bi.grams$bi.grams,
    bi.grams$Freq,
    scale = c(3, 1),
    min.freq = 3,
    max.words = 100,
    random.order = FALSE,
    rot.per = 0.3,
    colors = brewer.pal(8, "Dark2"))