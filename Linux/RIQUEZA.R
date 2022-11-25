#---------------------------Metadoon Estats------------------------------------#
library(tidyverse)
library(tidyr)
library(fossil)
library(ggplot2)
#---------------------------Universal objects----------------------------------#
set.seed(1976062000)
#entrada:
nome_diretorio <-getwd()
data_name <-"Metarquivos/Tabela_de_OTU/otutable.tsv"
pure_data <- paste(nome_diretorio, data_name, sep = "/")
#saida:
saida <- "Metarquivos/Graficos/RIQUEZA.png"
dir_saida <- paste(nome_diretorio, saida, sep = "/")
#-----------------------------Writing Data-------------------------------------#
#pegando a ultima coluna dos dados
columname <-read_tsv(pure_data)
names_in_columns<-colnames(columname)
#coletando inicio:fim da tabela
begin<-names_in_columns[2]
end_ing <- names_in_columns[length(names_in_columns)]
#estruturando tabela
data_1 <-read_tsv(pure_data)%>%
  pivot_longer(
    cols = begin:end_ing,
    names_to = "Group",
    values_to = "value"
  )
colnames(data_1) <- c('name','Group','value')
data_f <- data_1[, c("Group","name","value")]
rm(data_1)
#---------------------------Creating Functions---------------------------------#
#Richness
richness <- function(x){
  
  sum(x>0)
}
# -----------------------------Calculating-------------------------------------#
prich<-data_f %>%
  group_by(Group) %>%
  summarize(Riqueza = richness(value),
            n = sum(value)) %>%
  pivot_longer(cols=c(Riqueza),
               names_to="metric")
pl<-ggplot(prich, aes(y = value, x = Group, fill = value)) +
  geom_bar(stat = "identity") +
  xlab("Samples") + 
  ylab("Richness") 

pl
ggsave(filename = dir_saida, plot = pl)

