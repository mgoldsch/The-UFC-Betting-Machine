#! /usr/bin/Rscript

#Glicko Rating Generation

#load glicko library
library(PlayerRatings)
#path library
library(this.path)

#get path of csv data
path <- this.dir()

#load ufc data
ufc_data <- read.csv(paste0(path, "/test_data.csv"))[, c("fighter_1", "fighter_2", "winner", "date")]

#data prep
#drop NC results
ufc_data <- ufc_data[!ufc_data$winner == "NC", ]
#rename columns
colnames(ufc_data)[1] <- "R_fighter"
colnames(ufc_data)[2] <- "B_fighter"
#get numerical win values
ufc_data$R_win <- 0
ufc_data$R_win[which(ufc_data$winner == ufc_data$R_fighter)] <- 1
ufc_data$R_win[which(ufc_data$winner == "Draw")] <- .5

ufc_data$B_win <- 0
ufc_data$B_win[which(ufc_data$winner == ufc_data$B_fighter)] <- 1
ufc_data$B_win[which(ufc_data$winner == "Draw")] <- .5

#dorder by date
ufc_data$date <- as.Date(ufc_data$date, "%B %d, %Y")
ufc_data <- ufc_data[order(ufc_data$date), ]


#glicko
status_df <- NULL
glicko_rating <- NULL

for(j in 1:nrow(ufc_data)){
  #fight
  fight <- ufc_data[j, c("date", "R_fighter", "B_fighter", "R_win")]
  fight$date <- as.numeric(fight$date)
  
  #rating generation
  gl <- glicko(fight, status = status_df, init = c(1500, 290), cval = 5)
  
  #status for future input
  status_df <- gl$ratings
}

write.csv(status_df, paste0(path, "/glicko_rating/glicko_rating.csv"), row.names = FALSE)
