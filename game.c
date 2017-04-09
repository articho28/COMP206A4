#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//Functions
int getInv(char *input, int mannaOrGold);
void refresh(char *message, int manna, int gold);
int getCSV(int choice);
void updateCSV(int manna, int gold, int occupied);

int main(){

	//Variables to be used.
	char *data = getenv("QUERY_STRING");	
	char buffer[256];
	char *token;
	char command[20];
	char inventory[20];
	char URL[100];
	int manna;
	int gold;
	
	/*	
	printf("Content-type:text/html\n\n"); //Move down later.
	printf("<htm>It works! Your string is: %s", data);
	*/

	//Copy data to Buffer.
	strncpy(buffer, data, 255);
	
	//Get the command.
	token = strtok(buffer, "&");
	sscanf(token, "input=%s", command);
	
	//Get the inventory String (CSV)
	token = strtok(NULL, "&");
	sscanf(token, "inventory=%s", inventory);

	updateCSV(1, 2, 3);
	
	manna = getInv(inventory, 0);
	gold = getInv(inventory, 1);
	int roomManna = getCSV(0);
	int roomGold = getCSV(1);
	int roomOccupied = getCSV(2);

	/*
	printf("<p>Your command is: %s <br/> Your inventory CSV is: %s </p>", command, inventory);
	printf("<p>Your manna is: %d <br/> Your gold is: %d </p>", manna, gold);
	printf("<h2>Your room resources...</h2><p>Manna: %d</br>Gold: %d</br>Occupied: %d</p>", roomManna, roomGold, roomOccupied);
	printf("</html>");
	*/

	refresh("We did it!", 5, 5);

	return 1;


}

//Regenerates page with inventory preserved.
void refresh(char *message, int manna, int gold){
	
	//Make sure room is set to occupied.
	int occ = getCSV(2);
	if(occ = 0){
		updateCSV(getCSV(0), getCSV(1), 1);
	}
	
	//See if they win.
	if(gold >= 100){
		//Run win page
	}

	//Re-write page.	
	printf("Content-type:text/html\n\n");

	
	printf("<html>");
	printf("<head>");
	printf("<title>Dan's and Arty's Room</title>");
	printf("<style type=\"text/css\">body {background-color: #CCCCCC}#center {position: relative; top: 20px;}</style>");
	printf("</head>");
	printf("<body>");
	printf("<!-- This is the image -->");	
	printf("<center><img src=\"http://www.brandonhall.com/blogs/wp-content/uploads/2013/09/classroom-1.jpg\" width=\"666\" height=\"500\"></center>");	
	printf("<!-- This is the header -->");
	printf("<hr/><center>");
	printf("<h1 title=\"This is the best room.\">This is the math room.</h1><h2> %s </h2>",message);
	printf("</center><hr/>");
	printf("<!-- This is the North button -->");
	printf("<center><form action=\"cgi-bin/a.out.cgi\" method=\"get\">");
	printf("<input type=\"submit\" name=\"input\" value=\"North\">");	
	printf("<input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">", manna, gold);
	printf("<input type=\"hidden\" name=\"URL\" value=\"http://www.cs.mcgill.ca/~dvanac\">");
	printf("</form></center>");
	printf("<!-- This is the West button, East button, textbox, and submit button. -->");
	printf("<center><form action=\"cgi-bin/a.out.cgi\" method=\"get\" style=\"display: inline;\">");
	printf("<input type=\"submit\" name=\"input\" value=\"West\">");	
	printf("<input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">", manna, gold);
	printf("<input type=\"hidden\" name=\"URL\" value=\"http://www.cs.mcgill.ca/~dvanac\">");
	printf("</form>");
	printf("<form action=\"cgi-bin/a.out.cgi\" method=\"get\" style=\"display: inline;\">");
	printf("<input type=\"text\" name=\"input\"><input type=\"submit\" value=\"submit\">");		
	printf("<input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">", manna, gold);
	printf("</form>");
	printf("<form action=\"cgi-bin/a.out.cgi\" method=\"get\" style=\"display: inline;\">");	
	printf("<input type=\"submit\" name=\"input\" value=\"East\">");	
	printf("<input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">", manna, gold);
	printf("<input type=\"hidden\" name=\"URL\" value=\"http://www.cs.mcgill.ca/~dvanac\">");
	printf("</form></center>");
	printf("<!-- This is the South button -->");
	printf("<center><div id=\"center\">");
	printf("<form action=\"cgi-bin/transporter.py\" method=\"get\">");
	printf("<input type=\"submit\" name=\"input\" value=\"South\">");	
	printf("<input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">", manna, gold);
	printf("<input type=\"hidden\" name=\"URL\" value=\"http://www.cs.mcgill.ca/~dvanac\">");
	printf("</form>");
	printf("</div></center>");
	printf("</body>");
	printf("</html>");

}

//Gets data from CSV file. Choice dictates what value we get (0 is manna, 1 is gold, 2 is occupied)
int getCSV(int choice){
	
	//Preps file for reading	
	FILE *in;
	in = fopen("resources.csv", "r+");
	
	//Values to get
	int manna, gold, occupied;
	
	//Used for reading file.
	char temp[50];
	char *string;
	char ch;
	int i = 0;
	
	//Used for seperating values by commas.
	char *token;	
	
	//Gets Data from file as one string
	while((ch=fgetc(in)) != EOF){
		temp[i]=ch;
		i++;
	}
	string = temp;
	fclose(in);	
	
	//Seperates by comma, and stores in appropriate variables.
	i=0;
	token = strtok(string, ",");
	while(token != NULL){
		if(i==0){manna=atoi(token);}
		if(i==1){gold=atoi(token);}
		if(i==2){occupied=atoi(token);}
		i++;
		token = strtok(NULL, ",");
	}
	

	//Returns the desired value
	if(choice==0){
		return manna;
	}
	else if(choice==1){
		return gold;
	}
	else if(choice==2){
		return occupied;
	}
	else{
		return -1;
	}
}

//Updates CSV files based on choice (0 is manna, 1 is gold, 3 is occupied).
void updateCSV(int manna, int gold, int occupied){
		
	//Preps file for reading	
	FILE *out;
	out = fopen("resources.csv", "r+");
	truncate("resources.csv", 0);
	fprintf(out, "%d,%d,%d", manna, gold, occupied);
	fclose(out);
}

//Returns the players manna or gold.
int getInv(char *input, int mannaOrGold){
	
	char *mannaStr = malloc(256);
	char *goldStr = malloc(256);
	
	//Get manna value
	char *result = mannaStr;
	while(*input != '%'){
		*result = *input;
		result++;
		input++;
	}

	//Skip over %2C
	input+=3;
	
	result = goldStr;
	while(*input){
		*result = *input;
		result++;
		input++;
	}

	//Convert to int and return correct inventory item.
	if(mannaOrGold==0){
		int manna = atoi(mannaStr);
		return manna;
	}
	else if(mannaOrGold==1){
		int gold = atoi(goldStr);
		return gold;
	}
	else{
		return 0;
	}
}



















