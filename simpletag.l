letter [A-Za-z]
digit [0-9]
operator [<!\>\+\-=] 
%{
    #include <stdio.h>
    int Kcount;
    int Icount;
%}

%%
\n {printf("\n");fprintf(yyout,yytext);}
program {printf(" <function> ");fprintf(yyout," <function> ");}
set {printf(" <assignment> ");fprintf(yyout," <assignment> ");}
[Ii]f {printf(" <condition> ");fprintf(yyout," <condition> ");}
Do {printf(" <loop> ");fprintf(yyout," <loop> ");}
to {printf(" to ");fprintf(yyout," to ");}
is[\s ]divisible[\s ]by {printf(" <operator> ");fprintf(yyout," <operator> ");}
print {printf(" <keyword> <print> ");fprintf(yyout," <keyword> <print> ");}
({digit})+ {printf(" <int> ");fprintf(yyout," <int> ");}
auto|double|if|static|break|else|int|struct|case|enum|long|switch|char|extern|near|typedef|const|float|continue|register|union|unsigned|void|while|default|do|goto|signed|while|signed  {++Kcount;printf(" <keyword> ");fprintf(yyout," <keyword> ");}
{operator} {printf(" <operator> ");fprintf(yyout," <operator> ");}//,yytext);}
\"(\\.|[^"\\])*\" {printf("String:\t%s",yytext);fprintf(yyout,"<string>");}
\'[a-zA-Z0-9.]\' {printf("Character:\t%s",yytext);fprintf(yyout,yytext);}
{letter}({letter}|{digit}|_)*  {printf(" <identifier> ",yytext);fprintf(yyout," <identifier> ");}
[.*] {fprintf(yyout,yytext);} 
%%
int main()
{
    yyin = fopen("t1.pc","r");
    yyout = fopen("output.txt","w");
    yylex();
    fclose(yyin);
    return 0;

}
int yywrap()
{return(1);}