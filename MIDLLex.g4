lexer grammar MIDLLex;

fragment LETTER
    : [a-z]
    | [A-Z]
    ;

fragment DIGIT
    : [0-9]
    ;

fragment UNDERLINE
    : '_'
    ;


fragment INTEGER_TYPE_SUFFIX
    : 'l'
    | 'L'
    ;

INTEGER
    : ('0'|[1-9][0-9]*)INTEGER_TYPE_SUFFIX?
    ;

fragment EXPONENT
    : ('e'|'E')('+'|'-')?[0-9]+
    ;

fragment FLOAT_TYPE_SUFFIX
    : 'f'
    | 'F'
    | 'd'
    | 'D'
    ;

FLOATING_PT
    : [0-9]+ '.' [0-9]*  EXPONENT?  FLOAT_TYPE_SUFFIX?
    | '.' [0-9]+  EXPONENT?  FLOAT_TYPE_SUFFIX?
    | [0-9]+  EXPONENT  FLOAT_TYPE_SUFFIX?
    | [0-9]+  EXPONENT?  FLOAT_TYPE_SUFFIX
    ;

fragment ESCAPE_SEQUENCE
    : '\\' ('b' | 't' | 'n' | 'f' | 'r' | '"' | '\'' | '\\')
    ;

CHAR
    : '\'' (ESCAPE_SEQUENCE | ( ~'\\' | ~'\'' )) '\''
    ;

STRING
    : '"' (ESCAPE_SEQUENCE | ( ~'\\' | ~'"' ))* '"'
    ;

BOOLEAN
    : 'true'
    | 'false'
    | 'TRUE'
    | 'FALSE'
    ;

ID
    : LETTER ( UNDERLINE ? (LETTER | DIGIT))*
    ;
















