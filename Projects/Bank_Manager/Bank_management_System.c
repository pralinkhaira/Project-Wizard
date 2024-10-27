/* Bank Management System  */

#include <stdio.h>
#include<string.h>
#include<direct.h>

char filename[500];

typedef struct customer
{
  int bank_acc;
  char name[50];
  float balance;
} C;

int acc_serialget();
int acc_serialput(int);
void display_Option();
void create_account(C c1);
float deposit();
float withdraw();
float balance_Inquiry();
int download_data();

int acc_serialget()
{
  int acc_no;
  FILE *acc_no_file;
  acc_no_file = fopen("acc_no_serial.txt", "r");
  if(acc_no_file==NULL){
    acc_no_file = fopen("acc_no_serial.txt", "w");
    fprintf(acc_no_file,"1"); 
  }
  fscanf(acc_no_file, "%d", &acc_no);
  fclose(acc_no_file);
  return acc_no;
}

int acc_serialput(int a)
{
  int acc_no;
  FILE *acc_no_file;
  acc_no_file = fopen("acc_no_serial.txt", "w");
  fprintf(acc_no_file, "%d", a + 1);
  fclose(acc_no_file);
  return 0;
}

void display_Option()
{
    printf("\n      Welcome To AU Bank\n\n");
    printf("  BBBB      A      N   N  K  K  \n");
    printf("  B   B    A A     NN  N  K  K  \n");
    printf("  BBBB    A   A    N N N  KKK   \n");
    printf("  B   B  AAAAAAA   N  NN  K  K  \n");
    printf("  BBBB  A       A  N   N  K   K   Bank Code => 100\n\n");
    printf("Made By Amit Sharma         Github:- Darkforce112 \n\n");
  printf("Options are\n");
  printf("1 = Create Account\n");
  printf("2 = Deposit\n");
  printf("3 = Withdraw\n");
  printf("4 = Balance Inquiry\n");
  printf("5 = Save/Load Data\n");
}

void create_account(C c1)
{
  int acc_no = acc_serialget();
  printf("Enter Details\n");
  printf("Enter Customer Name : ");
  fgets(c1.name,sizeof(c1.name),stdin);
  c1.name[strcspn(c1.name, "\n")] = '\0';
 if (fgets(c1.name, sizeof(c1.name), stdin) == NULL) {
        printf("Error\n");
    }
  printf("Enter  initial Balance  : Rs ");
  scanf("%f", &c1.balance);
  c1.bank_acc = 1000 + acc_no;
  acc_serialput(acc_no);
  printf("Your Account Number : %d\n", c1.bank_acc);
  FILE *db;
  db = fopen("database_accounts.txt", "a");
  fprintf(db, " Serial No. : %d\n Name : %s Account Number : %d\n Balance : %.2f\n\n\n", acc_no, c1.name, c1.bank_acc, c1.balance);
  FILE *ptr;
  FILE *check;
  check=fopen("balance","r");
  if(check==NULL){
 _mkdir("balance");
  }
  snprintf(filename, sizeof(filename), "balance/filename_%d.txt", acc_no);
  ptr = fopen(filename, "w");
  fprintf(ptr, "%f", c1.balance);
  fclose(check);
  fclose(ptr);

  check=fopen("customer","r");
  if(check==NULL){
 _mkdir("customer");
  }
  snprintf(filename, sizeof(filename), "customer/user_%d.txt", acc_no);
  ptr = fopen(filename, "w");
  fprintf(ptr, "%s", c1.name);
  fclose(check);
    fclose(ptr);
}

float balance_Inquiry()
{
  int bank_ac_no;
  float balance;
  printf("Enter Your account Number : ");
  scanf("%d", &bank_ac_no);
  FILE *file;
  snprintf(filename, sizeof(filename), "balance/filename_%d.txt", bank_ac_no - 1000);
  file = fopen(filename, "r");
  if (file == NULL)
  {
    printf("User Not Exist");
    return 1;
  }
  fscanf(file, "%f", &balance);
  printf("Your Bank balance is %f\n", balance);
}

float deposit()
{
  float money, prev_balance;
  int bankacc_no;
  char cname[50];
  printf("Enter Your Account Number : ");
  scanf("%d", &bankacc_no);

  FILE *balance;
  snprintf(filename, sizeof(filename), "balance/filename_%d.txt", bankacc_no - 1000);
  balance = fopen(filename, "r");
  if (balance == NULL)
  {
    printf("User Not Exist");
    return 1;
  }
  printf("Enter Money you want to deposit : ");
  scanf("%f", &money);
  if(money<0){
    printf("\nYou try to deposit in negative Which is not possible");
    return 0.0;
  }
  fscanf(balance, "%f", &prev_balance);
  balance = fopen(filename, "w");
  fprintf(balance, "%f", prev_balance + money);

 FILE *db;
 FILE *name;
  db = fopen("database_accounts.txt", "a");
  snprintf(filename,sizeof(filename),"customer/user_%d.txt",bankacc_no-1000);
  name = fopen(filename, "r");
  fgets(cname,sizeof(cname), name);
  cname[strcspn(cname,"\n")]= '\0';
  fprintf(db, "Updated : \n Serial No. : %d\n Name : %s\n Account Number : %d\n Balance : %.2f\n\n\n", bankacc_no-1000,cname,bankacc_no, prev_balance+money);
fclose(db);
  printf("Your Current Balance is %f", prev_balance + money);
  return prev_balance+money;
}
float withdraw()
{
  float money, prev_balance;
  int bank_acc_no;
    char cname[50];
  printf("Enter Your Account Number : ");
  scanf("%d", &bank_acc_no);

  FILE *balance;
  snprintf(filename, sizeof(filename), "balance/filename_%d.txt", bank_acc_no - 1000);
  balance = fopen(filename, "r");
  if (balance == NULL)
  {
    printf("User Not Exist");
    return 1;
  }
  printf("Enter Money you want to deposit : ");
  scanf("%f", &money);
  fscanf(balance, "%f", &prev_balance);
  if (prev_balance < money)
  {
    printf("You have low balance");
    return 1;
  }
  balance = fopen(filename, "w");
  fprintf(balance, "%f", prev_balance - money);
FILE *db;
 FILE *name;
  db = fopen("database_accounts.txt", "a");
  snprintf(filename,sizeof(filename),"customer/user_%d.txt",bank_acc_no-1000);
  name = fopen(filename, "r");
  fgets(cname,sizeof(cname), name);
  cname[strcspn(cname,"\n")]= '\0';
  fprintf(db, "Updated : \n Serial No. : %d\n Name : %s\n Account Number : %d\n Balance : %.2f\n\n\n", bank_acc_no-1000,cname,bank_acc_no, prev_balance-money);
fclose(db);
  printf("Your Current Balance is %f", prev_balance - money);
}

int download_data()
{
  int i = 1, n, acc_no;
  char name[25];
  float balance;
  int serial = acc_serialget();

  printf("Enter customer Account Number : ");
  scanf("%d", &acc_no);

  if (acc_no - 1000 > serial)
  {
    printf("User Not Exist");
    return 1;
  }
  FILE *copy;
  snprintf(filename, sizeof(filename), "customer/user_%d.txt", acc_no - 1000);
  copy = fopen(filename, "r");
  fscanf(copy, "%s", &name);
  snprintf(filename, sizeof(filename), "balance/filename_%d.txt", acc_no - 1000);
  copy = fopen(filename, "r");
  fscanf(copy, "%f", &balance);

  printf("Choose Download Location\n 1 = Download Folder\n 2 = Choose location\n");

  while (i--)
  {
    scanf("%d", &n);
    if (n == 1)
    {
      char user[35];
      printf("Enter Your device Username(i.e hp, default,vivo,mac etc) : ");
      scanf("%s", user);
      FILE *download;
      snprintf(filename, sizeof(filename), "C:/Users/%s/Downloads/user_%d.txt", user, acc_no);
      download = fopen(filename, "w");
      fprintf(download, "Name = %s\nAccount Number = %d\nBalance = %f", name, acc_no, balance);
      printf("Download Sucessfully");
    }
    else if (n == 2)
    {
      char here[100];
      printf("Enter Download location(Full path) : ");
      scanf("%s", here);
      FILE *download;
      snprintf(filename, sizeof(filename), "%s", here);
      download = fopen(filename, "w");
      fprintf(download, "Name = %s\nAccount Number = %d\nBalance = %f", name, acc_no, balance);
      printf("Download Sucessfully");
    }
    else
    {
      printf("Choose Only 1 or 2");
      i++;
    }
  }

  return 0;
}

int main()
{
  int t;
  display_Option();

  int choose, i = 1;
  C c1;

  while (i--)
  {
    printf("Choose any Option : ");
    scanf("%d", &choose);
    switch (choose)
    {
    case 1:
      create_account(c1);
      break;
    case 2:
      deposit();
      break;
    case 3:
      withdraw();
      break;
    case 4:
      balance_Inquiry();
      break;
    case 5:
      download_data();
      break;
    default:
      printf("You enter Wrong Option\n");
      i++;
    }
  }

  return 0;
}