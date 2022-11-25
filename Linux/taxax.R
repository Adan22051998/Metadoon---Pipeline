set.seed(1976062000)

#libraries


library(tidyverse)
library(tidyr)
library(dplyr)
library(readr)
library(stringr)
library(ggplot2)

#reading files
PURE_OTU_FILE <-read_tsv(file = "/home/adanrdo/Documentos/SAMPLES/taxa/otutable.tsv")
OTUs<-arrange_all(PURE_OTU_FILE)
PURE_TAXA_FILES <-read_tsv(file = "/home/adanrdo/Documentos/SAMPLES/taxa/taxonomy_mangrove.tsv", col_names = FALSE)
rownames_1 <-c("Kingdom","Phylum", "Class","Order","Family","Genre", "Species", "null")
tf_pure <-arrange(PURE_TAXA_FILES,X1,X2)
X2_<- tibble(tf_pure$X2)
taxo1<-str_split_fixed(X2_$`tf_pure$X2`, ",", 8)
colnames(taxo1)<-(rownames_1)
DF_TAXONOMY <- data.frame(taxo1)
phyl <- tibble(DF_TAXONOMY$Phylum)
colnames(phyl)<-(rownames_1[2])
phylu <-data.frame(phyl)
hylum<-tibble(gsub('p:','', phylu$Phylum))
ylum<-tibble(gsub('"', '', hylum$`gsub("p:", "", phylu$Phylum)`))
colnames(ylum) <-(rownames_1[2])
TAXONOMY <-data.frame(ylum)

tabela_0 <- tibble(tf_pure$X1, ylum$Phylum)
colnames(tabela_0)<-c("#OTU ID", "Phylum")
######################################################################

names_in_columns<-colnames(OTUs)
#coletando inicio:fim da tabela
begin<-names_in_columns[2]
end_ing <- names_in_columns[length(names_in_columns)]
TAP<-tibble(gsub('.(([0-9]))', '',tabela_0$Phylum))
TAP<-data.frame(gsub('0)', '',TAP$`gsub(".(([0-9]))", "", tabela_0$Phylum)`))
colnames(TAP) <-(rownames_1[2])
TAB0<- data.frame(tabela_0$`#OTU ID`, TAP)
NAMES_<- c(names_in_columns[1],rownames_1[2])
colnames(TAB0) <-(NAMES_)
table_A<-full_join(TAB0, OTUs, by = "#OTU ID")
TABLE_ <-arrange_all(table_A)



######################################################################

#
number_in_cols<-tibble(TABLE_%>% select(begin:end_ing))
soma_<- number_in_cols %>%
  replace(is.na(.), 0)%>%
  summarise_all(sum)

x_ <- data.frame(lst(colnames(TABLE_)))
x_ <- x_[-1,]
x_ <- x_[-1]
l_x_ <-length(x_)
y <-lst(x_[1:l_x_])
TABLE_$x_[1]
###########################################
#ploting
######################################################################
pl_13 <- TABLE_%>%
  pivot_longer(
    cols = Phylum,
    names_to = "Clade",
    values_to = "Phylum"
  )
rowSums(pl_13$Phylum == pl_13$Phylum)
PL_T<-xtabs(~Phylum, data = TAB0)
###############################################################################
#saida:
saida <- "Metarquivos/Graficos/TAX.png"
dir_saida <- paste(nome_diretorio, saida, sep = "/")

graphics.off()
png(filename = dir_saida, width = 1000, height = 1280, res = 260)
barplot(PL_T,
        horiz = TRUE,
        xlab = "Frequency",
        cex=0.5,
        cex.axis =0.8,
        cex.names= 0.26,
        las=1,
        col = colors(),
        xlim = c(0, 5000),
        main = "Total Frequency (Phylum)",
        sub = "Phylum/OTUs",
        axisnames = TRUE)

barplot(PL_T,
        horiz = TRUE,
        xlab = "Frequency",
        cex=0.5,
        cex.axis =0.8,
        cex.names= 0.26,
        las=1,
        col = colors(),
        xlim = c(0, 5000),
        main = "Total Frequency (Phylum)",
        sub = "Phylum/OTUs",
        axisnames = TRUE,
        add = TRUE)
grid(nx=NA, ny=NULL)
dev.off()
###############################################################################