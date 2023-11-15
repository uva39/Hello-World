setwd("/Users/uva/Downloads")

A <- vector()
B <- vector()
for (f in list.files(path='./09_data01', pattern='[.]txt$')){
    file <- scan(file = paste0("./09_data01/", f), what = 'char', quote = NULL)
    filenum = as.numeric(grep("^[0-9]", f, value = T))
    print(filenum)
    if (filenum %% 2 == 1){
        A <- c(A, file)
    }
    else {
        B <- c(B, file)
    }
}
print(length(A))
print(length(B))