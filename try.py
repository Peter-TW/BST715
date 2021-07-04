import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_excel("britishtouring.xlsx")
data1=pd.read_excel("inventory.xlsx")

###Inventory (Figure 13)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Cabin"],marker="o",alpha=0.7,label="Cabin")
# for x1,y1 in enumerate(data1["Cabin"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=8)
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=8)
# sns.lineplot(x=data1["Round"],y=data1["Briefcase"],marker="o",alpha=0.7,label="Briefcase")
# for x1,y1 in enumerate(data1["Briefcase"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=8)
# plt.ylabel("Volume")
# plt.xlabel("Round")
# plt.title("Products Inventory ")
# plt.legend(loc="best")
# plt.show()

###shareholders report (Figure 12)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Forward Guidance"],marker="o",alpha=0.7,label="Forward Guidance")
# for x1,y1 in enumerate(data1["Forward Guidance"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"], y=data1["Dividend Rate"], marker="o",alpha=0.7,label="Dividend Rate")
# for x1,y1 in enumerate(data1["Dividend Rate"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# plt.ylabel("Score ")
# plt.xlabel("Round")
# plt.title("Shareholder Report")
# plt.legend(loc="best")
# plt.show()

###share price (Figure 11)
# sns.set()
# sns.lineplot(x=data["IncomeStatement"],y=data["Share price"],marker="o")
# for x1,y1 in enumerate(data["Share price"]):
#     plt.text(x1,y1*1.005,y1,ha="center")
# plt.ylabel("Price $")
# plt.xlabel("Round")
# plt.title("Share Price")
# plt.show()

###Salespeople cap (Figure 10)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Cabin"],marker="o",alpha=0.7,label="Cabin")
# for x1,y1 in enumerate(data1["Cabin"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"],y=data1["Briefcase"],marker="o",alpha=0.7,label="Briefcase")
# for x1,y1 in enumerate(data1["Briefcase"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# plt.ylabel("Score ")
# plt.xlabel("Round")
# plt.title("Salespeople Capability")
# plt.legend(loc="best")
# plt.show()

##HR (Figure 9)
# sns.set()
# sns.lineplot(x=data["IncomeStatement"],y=data["Human resources"],marker="o")
# for x1,y1 in enumerate(data["Human resources"]):
#     plt.text(x1,y1*1.005,y1,ha="center")
# plt.ylabel("Score")
# plt.xlabel("Round")
# plt.title("Human Resources Score")
# plt.show()

###Message (Figure 8)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Cabin"],marker="o",alpha=0.7,label="Cabin")
# for x1,y1 in enumerate(data1["Cabin"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"],y=data1["Briefcase"],marker="o",alpha=0.7,label="Briefcase")
# for x1,y1 in enumerate(data1["Briefcase"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# plt.ylabel("Score ")
# plt.xlabel("Round")
# plt.title("Message Score")
# plt.legend(loc="center right")
# plt.show()

##brand (Figure 7)
# sns.set()
# sns.lineplot(x=data["IncomeStatement"],y=data["Brand Awareness"],marker="o")
# for x1,y1 in enumerate(data["Brand Awareness"]):
#     plt.text(x1,y1*1.005,y1,ha="center")
# plt.ylabel("Score")
# plt.xlabel("Round")
# plt.title("Brand Awareness Score")
# plt.show()

##Stock (Figure 6)
# sns.set()
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# plt.ylabel("Stock out ")
# plt.xlabel("Round")
# plt.title("Stock out on Holdall")
# plt.show()

###Price score (figure 5)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Cabin"],marker="o",alpha=0.7,label="Cabin")
# for x1,y1 in enumerate(data1["Cabin"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"],y=data1["Briefcase"],marker="o",alpha=0.7,label="Briefcase")
# for x1,y1 in enumerate(data1["Briefcase"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# plt.ylabel("Price $ ")
# plt.xlabel("Round")
# plt.title("Price ")
# plt.show()

###Price score (figure 4)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Cabin"],marker="o",alpha=0.7,label="Cabin")
# for x1,y1 in enumerate(data1["Cabin"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"],y=data1["Briefcase"],marker="o",alpha=0.7,label="Briefcase")
# for x1,y1 in enumerate(data1["Briefcase"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# plt.ylabel("Price $ ")
# plt.xlabel("Round")
# plt.title("Price Score ")
# plt.show()

###Product rate (Figure 3)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Cabin"],marker="o",alpha=0.7,label="Cabin")
# for x1,y1 in enumerate(data1["Cabin"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=8)
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=8)
# sns.lineplot(x=data1["Round"],y=data1["Briefcase"],marker="o",alpha=0.7,label="Briefcase")
# for x1,y1 in enumerate(data1["Briefcase"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=8)
# sns.lineplot(x=data1["Round"],y=data1["Total"],marker="o",linewidth = 3,label="Total")
# for x1,y1 in enumerate(data1["Total"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=8)
# plt.ylabel("Score")
# plt.xlabel("Round")
# plt.title("Product Rate Score")
# plt.show()

# ###Product sale (Figure 2)
# sns.set()
# sns.lineplot(x=data1["Round"],y=data1["Cabin"],marker="o",alpha=0.7,label="Cabin")
# for x1,y1 in enumerate(data1["Cabin"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"], y=data1["Holdall"], marker="o",alpha=0.7,label="Holdall")
# for x1,y1 in enumerate(data1["Holdall"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# sns.lineplot(x=data1["Round"],y=data1["Briefcase"],marker="o",alpha=0.7,label="Briefcase")
# for x1,y1 in enumerate(data1["Briefcase"]):
#     plt.text(x1,y1*1.005,y1,ha="center",fontsize=10)
# plt.ylabel("$ Million")
# plt.xlabel("Round")
# plt.title("Product Revenue")
# plt.show()

###sales, cach (Figure 1)
# sns.set()
# sns.lineplot(x=data["IncomeStatement"],y=data["Sales"],marker="o",label="Revenue")
# for x1,y1 in enumerate(data["Sales"]):
#     plt.text(x1,y1*1.015,y1,ha="center")
# sns.lineplot(x=data["IncomeStatement"],y=data["Net Income"],marker="o",label="Net Income")
# for x1,y1 in enumerate(data["Net Income"]):
#     plt.text(x1,y1*1.015,y1,ha="center")
# sns.lineplot(x=data["IncomeStatement"],y=data["Cash"],marker="o",label="Cash")
# for x1,y1 in enumerate(data["Cash"]):
#     plt.text(x1,y1*1.015,y1,ha="center")
# plt.legend(loc="best")
# plt.ylabel("£ million")
# plt.xlabel("Round")
# plt.title("British Touring")
# plt.show()

