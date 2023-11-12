library(wordcloud)
setwd("/Users/uva/Downloads")

TEXT <- scan(file = "07_data01.txt", what = "character", quote = NULL) # nolint
TEXT <- iconv(TEXT, from = "iso-8859-1", to = "UTF-8") # nolint # nolint

TEXT <- gsub("^[[:punct:]]+|[[:punct:]]+$", "", TEXT) # nolint
TEXT <- tolower(TEXT) # nolint

bi.grams <- paste(TEXT[1:length(TEXT)-1], TEXT[2:length(TEXT)], sep=" ") # nolint
bi.grams <- table(bi.grams) # nolint
bi.grams <- data.frame(bi.grams) # nolint

wordcloud(
    bi.grams$bi.grams, # nolint
    bi.grams$Freq,
    scale = c(3, 1),
    min.freq = 3,
    max.words = 100,
    random.order = FALSE,
    rot.per = 0.3,
    colors = brewer.pal(8, "Dark2"))