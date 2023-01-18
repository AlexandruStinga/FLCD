%{
#include <stdio.h>
%}

%start cmpdstmt
%token DIGIT 
%token LETTER 
%token AND 
%token OR 
%token IF 
%token ELSE 
%token FOR 
%token NUMBER 
%token STRING 
%token WHILE 
%token READ 
%token PRINT 
%token SQRT 
%token PLUS 
%token MINUS 
%token MUL 
%token DIV 
%token MOD 
%token EQ 
%token NEQ 
%token GT 
%token GTE 
%token LT 
%token LTE 
%token DOUBLEEQ 
%token COMMA 
%token DOT_COMMA 
%token CURLY_BRACKET_RIGHT 
%token CURLY_BRACKET_LEFT 
%token ROUND_BRACKET_RIGHT 
%token ROUND_BRACKET_LEFT 
%token RIGHT_BRACKET_RIGHT 
%token RIGHT_BRACKET_LEFT
%TOKEN ID

%left '+' 
%left '-' 
%left '*' 
%left '/' 
%left '%'
%left '=' 
%left '>=' 
%left '<=' 
%left '>' 
%left '<' 
%left '==' 
%left '!='

%%                   

cmpdstmt: '{' stmtlist '}'
        ,
type: "number" | "string" | array_declaration
        ,
array_declaration: "number" "[" DIGIT "]"
        ,
readstmt: "read(" ID ")"
        ,
declaration: type ' ' ID
        ,
decllist: declaration | declaration ", " decllist
        ,
printstmt: "print(" ID ")" | "print(" DIGIT ")"
        ,
relation: "<" | "<=" | "==" | "!=" | ">=" | ">"
        ,
expression: expression "+" term | expression "-" term | term
        ,
term: term "*" factor | term "/" factor | factor
        ,
factor: "(" expression ")" | DIGIT | ID
        ,
stmtlist: stmt | stmt ";" stmtlist
        ,
stmt: simplestmt | structstmt
        ,
simplestmt: assignstmt ";" | readstmt ";" | printstmt ";" | declaration ";"
        ,
structstmt: cmpdstmt | ifstmt | forstmt | whilestmt
        ,
assignstmt: ID "=" expression
        ,
ifstmt: "if" condition stmt | "if" condition stmt "else" stmt
        ,
condition: "(" expression relation expression ")"
        ,
forstmt: "for" "(" "number" assignstmt ";" condition ";" assignstmt ")" stmt
        ,
whilestmt: "while" condition stmt
        ,
sqrtstmt: "sqrt(" DIGIT ")" | "sqrt(" ID ")"
        ,
%%
main()
{
 return(yyparse());
}
yyerror(s)
char *s;
{
  fprintf(stderr, "%s\n",s);
}
yywrap()
{
  return(1);
}