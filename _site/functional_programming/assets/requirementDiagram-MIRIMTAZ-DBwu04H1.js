import{_ as t,g as e,s as i,a as n,b as r,c as s,d as a,v as o,l,j as h}from"./mermaid-D0MGOvVE.js";import{s as c}from"./transform-CdY8z5kT.js";import{G as u}from"./graph-XoNMemoA.js";import{l as d}from"./layout-D3QmwxRU.js";import{l as p}from"./step-xJWGRC3d.js";import"./index-BiV-b1K2.js";import"./_baseUniq-DUj_-ybn.js";import"./_baseEach-DDZLUgL5.js";import"./min-FhCtSWQU.js";import"./_baseMap-CoUfqKnE.js";import"./sortBy-CHDem8Sy.js";var y=function(){var e=t((function(t,e,i,n){for(i=i||{},n=t.length;n--;i[t[n]]=e);return i}),"o"),i=[1,3],n=[1,4],r=[1,5],s=[1,6],a=[5,6,8,9,11,13,31,32,33,34,35,36,44,62,63],o=[1,18],l=[2,7],h=[1,22],c=[1,23],u=[1,24],d=[1,25],p=[1,26],y=[1,27],_=[1,20],g=[1,28],E=[1,29],m=[62,63],R=[5,8,9,11,13,31,32,33,34,35,36,44,51,53,62,63],f=[1,47],I=[1,48],S=[1,49],b=[1,50],N=[1,51],T=[1,52],k=[1,53],x=[53,54],A=[1,64],w=[1,60],q=[1,61],v=[1,62],$=[1,63],O=[1,65],L=[1,69],C=[1,70],M=[1,67],F=[1,68],D=[5,8,9,11,13,31,32,33,34,35,36,44,62,63],P={trace:t((function(){}),"trace"),yy:{},symbols_:{error:2,start:3,directive:4,NEWLINE:5,RD:6,diagram:7,EOF:8,acc_title:9,acc_title_value:10,acc_descr:11,acc_descr_value:12,acc_descr_multiline_value:13,requirementDef:14,elementDef:15,relationshipDef:16,requirementType:17,requirementName:18,STRUCT_START:19,requirementBody:20,ID:21,COLONSEP:22,id:23,TEXT:24,text:25,RISK:26,riskLevel:27,VERIFYMTHD:28,verifyType:29,STRUCT_STOP:30,REQUIREMENT:31,FUNCTIONAL_REQUIREMENT:32,INTERFACE_REQUIREMENT:33,PERFORMANCE_REQUIREMENT:34,PHYSICAL_REQUIREMENT:35,DESIGN_CONSTRAINT:36,LOW_RISK:37,MED_RISK:38,HIGH_RISK:39,VERIFY_ANALYSIS:40,VERIFY_DEMONSTRATION:41,VERIFY_INSPECTION:42,VERIFY_TEST:43,ELEMENT:44,elementName:45,elementBody:46,TYPE:47,type:48,DOCREF:49,ref:50,END_ARROW_L:51,relationship:52,LINE:53,END_ARROW_R:54,CONTAINS:55,COPIES:56,DERIVES:57,SATISFIES:58,VERIFIES:59,REFINES:60,TRACES:61,unqString:62,qString:63,$accept:0,$end:1},terminals_:{2:"error",5:"NEWLINE",6:"RD",8:"EOF",9:"acc_title",10:"acc_title_value",11:"acc_descr",12:"acc_descr_value",13:"acc_descr_multiline_value",19:"STRUCT_START",21:"ID",22:"COLONSEP",24:"TEXT",26:"RISK",28:"VERIFYMTHD",30:"STRUCT_STOP",31:"REQUIREMENT",32:"FUNCTIONAL_REQUIREMENT",33:"INTERFACE_REQUIREMENT",34:"PERFORMANCE_REQUIREMENT",35:"PHYSICAL_REQUIREMENT",36:"DESIGN_CONSTRAINT",37:"LOW_RISK",38:"MED_RISK",39:"HIGH_RISK",40:"VERIFY_ANALYSIS",41:"VERIFY_DEMONSTRATION",42:"VERIFY_INSPECTION",43:"VERIFY_TEST",44:"ELEMENT",47:"TYPE",49:"DOCREF",51:"END_ARROW_L",53:"LINE",54:"END_ARROW_R",55:"CONTAINS",56:"COPIES",57:"DERIVES",58:"SATISFIES",59:"VERIFIES",60:"REFINES",61:"TRACES",62:"unqString",63:"qString"},productions_:[0,[3,3],[3,2],[3,4],[4,2],[4,2],[4,1],[7,0],[7,2],[7,2],[7,2],[7,2],[7,2],[14,5],[20,5],[20,5],[20,5],[20,5],[20,2],[20,1],[17,1],[17,1],[17,1],[17,1],[17,1],[17,1],[27,1],[27,1],[27,1],[29,1],[29,1],[29,1],[29,1],[15,5],[46,5],[46,5],[46,2],[46,1],[16,5],[16,5],[52,1],[52,1],[52,1],[52,1],[52,1],[52,1],[52,1],[18,1],[18,1],[23,1],[23,1],[25,1],[25,1],[45,1],[45,1],[48,1],[48,1],[50,1],[50,1]],performAction:t((function(t,e,i,n,r,s,a){var o=s.length-1;switch(r){case 4:this.$=s[o].trim(),n.setAccTitle(this.$);break;case 5:case 6:this.$=s[o].trim(),n.setAccDescription(this.$);break;case 7:this.$=[];break;case 13:n.addRequirement(s[o-3],s[o-4]);break;case 14:n.setNewReqId(s[o-2]);break;case 15:n.setNewReqText(s[o-2]);break;case 16:n.setNewReqRisk(s[o-2]);break;case 17:n.setNewReqVerifyMethod(s[o-2]);break;case 20:this.$=n.RequirementType.REQUIREMENT;break;case 21:this.$=n.RequirementType.FUNCTIONAL_REQUIREMENT;break;case 22:this.$=n.RequirementType.INTERFACE_REQUIREMENT;break;case 23:this.$=n.RequirementType.PERFORMANCE_REQUIREMENT;break;case 24:this.$=n.RequirementType.PHYSICAL_REQUIREMENT;break;case 25:this.$=n.RequirementType.DESIGN_CONSTRAINT;break;case 26:this.$=n.RiskLevel.LOW_RISK;break;case 27:this.$=n.RiskLevel.MED_RISK;break;case 28:this.$=n.RiskLevel.HIGH_RISK;break;case 29:this.$=n.VerifyType.VERIFY_ANALYSIS;break;case 30:this.$=n.VerifyType.VERIFY_DEMONSTRATION;break;case 31:this.$=n.VerifyType.VERIFY_INSPECTION;break;case 32:this.$=n.VerifyType.VERIFY_TEST;break;case 33:n.addElement(s[o-3]);break;case 34:n.setNewElementType(s[o-2]);break;case 35:n.setNewElementDocRef(s[o-2]);break;case 38:n.addRelationship(s[o-2],s[o],s[o-4]);break;case 39:n.addRelationship(s[o-2],s[o-4],s[o]);break;case 40:this.$=n.Relationships.CONTAINS;break;case 41:this.$=n.Relationships.COPIES;break;case 42:this.$=n.Relationships.DERIVES;break;case 43:this.$=n.Relationships.SATISFIES;break;case 44:this.$=n.Relationships.VERIFIES;break;case 45:this.$=n.Relationships.REFINES;break;case 46:this.$=n.Relationships.TRACES}}),"anonymous"),table:[{3:1,4:2,6:i,9:n,11:r,13:s},{1:[3]},{3:8,4:2,5:[1,7],6:i,9:n,11:r,13:s},{5:[1,9]},{10:[1,10]},{12:[1,11]},e(a,[2,6]),{3:12,4:2,6:i,9:n,11:r,13:s},{1:[2,2]},{4:17,5:o,7:13,8:l,9:n,11:r,13:s,14:14,15:15,16:16,17:19,23:21,31:h,32:c,33:u,34:d,35:p,36:y,44:_,62:g,63:E},e(a,[2,4]),e(a,[2,5]),{1:[2,1]},{8:[1,30]},{4:17,5:o,7:31,8:l,9:n,11:r,13:s,14:14,15:15,16:16,17:19,23:21,31:h,32:c,33:u,34:d,35:p,36:y,44:_,62:g,63:E},{4:17,5:o,7:32,8:l,9:n,11:r,13:s,14:14,15:15,16:16,17:19,23:21,31:h,32:c,33:u,34:d,35:p,36:y,44:_,62:g,63:E},{4:17,5:o,7:33,8:l,9:n,11:r,13:s,14:14,15:15,16:16,17:19,23:21,31:h,32:c,33:u,34:d,35:p,36:y,44:_,62:g,63:E},{4:17,5:o,7:34,8:l,9:n,11:r,13:s,14:14,15:15,16:16,17:19,23:21,31:h,32:c,33:u,34:d,35:p,36:y,44:_,62:g,63:E},{4:17,5:o,7:35,8:l,9:n,11:r,13:s,14:14,15:15,16:16,17:19,23:21,31:h,32:c,33:u,34:d,35:p,36:y,44:_,62:g,63:E},{18:36,62:[1,37],63:[1,38]},{45:39,62:[1,40],63:[1,41]},{51:[1,42],53:[1,43]},e(m,[2,20]),e(m,[2,21]),e(m,[2,22]),e(m,[2,23]),e(m,[2,24]),e(m,[2,25]),e(R,[2,49]),e(R,[2,50]),{1:[2,3]},{8:[2,8]},{8:[2,9]},{8:[2,10]},{8:[2,11]},{8:[2,12]},{19:[1,44]},{19:[2,47]},{19:[2,48]},{19:[1,45]},{19:[2,53]},{19:[2,54]},{52:46,55:f,56:I,57:S,58:b,59:N,60:T,61:k},{52:54,55:f,56:I,57:S,58:b,59:N,60:T,61:k},{5:[1,55]},{5:[1,56]},{53:[1,57]},e(x,[2,40]),e(x,[2,41]),e(x,[2,42]),e(x,[2,43]),e(x,[2,44]),e(x,[2,45]),e(x,[2,46]),{54:[1,58]},{5:A,20:59,21:w,24:q,26:v,28:$,30:O},{5:L,30:C,46:66,47:M,49:F},{23:71,62:g,63:E},{23:72,62:g,63:E},e(D,[2,13]),{22:[1,73]},{22:[1,74]},{22:[1,75]},{22:[1,76]},{5:A,20:77,21:w,24:q,26:v,28:$,30:O},e(D,[2,19]),e(D,[2,33]),{22:[1,78]},{22:[1,79]},{5:L,30:C,46:80,47:M,49:F},e(D,[2,37]),e(D,[2,38]),e(D,[2,39]),{23:81,62:g,63:E},{25:82,62:[1,83],63:[1,84]},{27:85,37:[1,86],38:[1,87],39:[1,88]},{29:89,40:[1,90],41:[1,91],42:[1,92],43:[1,93]},e(D,[2,18]),{48:94,62:[1,95],63:[1,96]},{50:97,62:[1,98],63:[1,99]},e(D,[2,36]),{5:[1,100]},{5:[1,101]},{5:[2,51]},{5:[2,52]},{5:[1,102]},{5:[2,26]},{5:[2,27]},{5:[2,28]},{5:[1,103]},{5:[2,29]},{5:[2,30]},{5:[2,31]},{5:[2,32]},{5:[1,104]},{5:[2,55]},{5:[2,56]},{5:[1,105]},{5:[2,57]},{5:[2,58]},{5:A,20:106,21:w,24:q,26:v,28:$,30:O},{5:A,20:107,21:w,24:q,26:v,28:$,30:O},{5:A,20:108,21:w,24:q,26:v,28:$,30:O},{5:A,20:109,21:w,24:q,26:v,28:$,30:O},{5:L,30:C,46:110,47:M,49:F},{5:L,30:C,46:111,47:M,49:F},e(D,[2,14]),e(D,[2,15]),e(D,[2,16]),e(D,[2,17]),e(D,[2,34]),e(D,[2,35])],defaultActions:{8:[2,2],12:[2,1],30:[2,3],31:[2,8],32:[2,9],33:[2,10],34:[2,11],35:[2,12],37:[2,47],38:[2,48],40:[2,53],41:[2,54],83:[2,51],84:[2,52],86:[2,26],87:[2,27],88:[2,28],90:[2,29],91:[2,30],92:[2,31],93:[2,32],95:[2,55],96:[2,56],98:[2,57],99:[2,58]},parseError:t((function(t,e){if(!e.recoverable){var i=new Error(t);throw i.hash=e,i}this.trace(t)}),"parseError"),parse:t((function(e){var i=this,n=[0],r=[],s=[null],a=[],o=this.table,l="",h=0,c=0,u=a.slice.call(arguments,1),d=Object.create(this.lexer),p={yy:{}};for(var y in this.yy)Object.prototype.hasOwnProperty.call(this.yy,y)&&(p.yy[y]=this.yy[y]);d.setInput(e,p.yy),p.yy.lexer=d,p.yy.parser=this,void 0===d.yylloc&&(d.yylloc={});var _=d.yylloc;a.push(_);var g=d.options&&d.options.ranges;function E(){var t;return"number"!=typeof(t=r.pop()||d.lex()||1)&&(t instanceof Array&&(t=(r=t).pop()),t=i.symbols_[t]||t),t}"function"==typeof p.yy.parseError?this.parseError=p.yy.parseError:this.parseError=Object.getPrototypeOf(this).parseError,t((function(t){n.length=n.length-2*t,s.length=s.length-t,a.length=a.length-t}),"popStack"),t(E,"lex");for(var m,R,f,I,S,b,N,T,k={};;){if(R=n[n.length-1],this.defaultActions[R]?f=this.defaultActions[R]:(null==m&&(m=E()),f=o[R]&&o[R][m]),void 0===f||!f.length||!f[0]){var x="";for(S in T=[],o[R])this.terminals_[S]&&S>2&&T.push("'"+this.terminals_[S]+"'");x=d.showPosition?"Parse error on line "+(h+1)+":\n"+d.showPosition()+"\nExpecting "+T.join(", ")+", got '"+(this.terminals_[m]||m)+"'":"Parse error on line "+(h+1)+": Unexpected "+(1==m?"end of input":"'"+(this.terminals_[m]||m)+"'"),this.parseError(x,{text:d.match,token:this.terminals_[m]||m,line:d.yylineno,loc:_,expected:T})}if(f[0]instanceof Array&&f.length>1)throw new Error("Parse Error: multiple actions possible at state: "+R+", token: "+m);switch(f[0]){case 1:n.push(m),s.push(d.yytext),a.push(d.yylloc),n.push(f[1]),m=null,c=d.yyleng,l=d.yytext,h=d.yylineno,_=d.yylloc;break;case 2:if(b=this.productions_[f[1]][1],k.$=s[s.length-b],k._$={first_line:a[a.length-(b||1)].first_line,last_line:a[a.length-1].last_line,first_column:a[a.length-(b||1)].first_column,last_column:a[a.length-1].last_column},g&&(k._$.range=[a[a.length-(b||1)].range[0],a[a.length-1].range[1]]),void 0!==(I=this.performAction.apply(k,[l,c,h,p.yy,f[1],s,a].concat(u))))return I;b&&(n=n.slice(0,-1*b*2),s=s.slice(0,-1*b),a=a.slice(0,-1*b)),n.push(this.productions_[f[1]][0]),s.push(k.$),a.push(k._$),N=o[n[n.length-2]][n[n.length-1]],n.push(N);break;case 3:return!0}}return!0}),"parse")},V=function(){return{EOF:1,parseError:t((function(t,e){if(!this.yy.parser)throw new Error(t);this.yy.parser.parseError(t,e)}),"parseError"),setInput:t((function(t,e){return this.yy=e||this.yy||{},this._input=t,this._more=this._backtrack=this.done=!1,this.yylineno=this.yyleng=0,this.yytext=this.matched=this.match="",this.conditionStack=["INITIAL"],this.yylloc={first_line:1,first_column:0,last_line:1,last_column:0},this.options.ranges&&(this.yylloc.range=[0,0]),this.offset=0,this}),"setInput"),input:t((function(){var t=this._input[0];return this.yytext+=t,this.yyleng++,this.offset++,this.match+=t,this.matched+=t,t.match(/(?:\r\n?|\n).*/g)?(this.yylineno++,this.yylloc.last_line++):this.yylloc.last_column++,this.options.ranges&&this.yylloc.range[1]++,this._input=this._input.slice(1),t}),"input"),unput:t((function(t){var e=t.length,i=t.split(/(?:\r\n?|\n)/g);this._input=t+this._input,this.yytext=this.yytext.substr(0,this.yytext.length-e),this.offset-=e;var n=this.match.split(/(?:\r\n?|\n)/g);this.match=this.match.substr(0,this.match.length-1),this.matched=this.matched.substr(0,this.matched.length-1),i.length-1&&(this.yylineno-=i.length-1);var r=this.yylloc.range;return this.yylloc={first_line:this.yylloc.first_line,last_line:this.yylineno+1,first_column:this.yylloc.first_column,last_column:i?(i.length===n.length?this.yylloc.first_column:0)+n[n.length-i.length].length-i[0].length:this.yylloc.first_column-e},this.options.ranges&&(this.yylloc.range=[r[0],r[0]+this.yyleng-e]),this.yyleng=this.yytext.length,this}),"unput"),more:t((function(){return this._more=!0,this}),"more"),reject:t((function(){return this.options.backtrack_lexer?(this._backtrack=!0,this):this.parseError("Lexical error on line "+(this.yylineno+1)+". You can only invoke reject() in the lexer when the lexer is of the backtracking persuasion (options.backtrack_lexer = true).\n"+this.showPosition(),{text:"",token:null,line:this.yylineno})}),"reject"),less:t((function(t){this.unput(this.match.slice(t))}),"less"),pastInput:t((function(){var t=this.matched.substr(0,this.matched.length-this.match.length);return(t.length>20?"...":"")+t.substr(-20).replace(/\n/g,"")}),"pastInput"),upcomingInput:t((function(){var t=this.match;return t.length<20&&(t+=this._input.substr(0,20-t.length)),(t.substr(0,20)+(t.length>20?"...":"")).replace(/\n/g,"")}),"upcomingInput"),showPosition:t((function(){var t=this.pastInput(),e=new Array(t.length+1).join("-");return t+this.upcomingInput()+"\n"+e+"^"}),"showPosition"),test_match:t((function(t,e){var i,n,r;if(this.options.backtrack_lexer&&(r={yylineno:this.yylineno,yylloc:{first_line:this.yylloc.first_line,last_line:this.last_line,first_column:this.yylloc.first_column,last_column:this.yylloc.last_column},yytext:this.yytext,match:this.match,matches:this.matches,matched:this.matched,yyleng:this.yyleng,offset:this.offset,_more:this._more,_input:this._input,yy:this.yy,conditionStack:this.conditionStack.slice(0),done:this.done},this.options.ranges&&(r.yylloc.range=this.yylloc.range.slice(0))),(n=t[0].match(/(?:\r\n?|\n).*/g))&&(this.yylineno+=n.length),this.yylloc={first_line:this.yylloc.last_line,last_line:this.yylineno+1,first_column:this.yylloc.last_column,last_column:n?n[n.length-1].length-n[n.length-1].match(/\r?\n?/)[0].length:this.yylloc.last_column+t[0].length},this.yytext+=t[0],this.match+=t[0],this.matches=t,this.yyleng=this.yytext.length,this.options.ranges&&(this.yylloc.range=[this.offset,this.offset+=this.yyleng]),this._more=!1,this._backtrack=!1,this._input=this._input.slice(t[0].length),this.matched+=t[0],i=this.performAction.call(this,this.yy,this,e,this.conditionStack[this.conditionStack.length-1]),this.done&&this._input&&(this.done=!1),i)return i;if(this._backtrack){for(var s in r)this[s]=r[s];return!1}return!1}),"test_match"),next:t((function(){if(this.done)return this.EOF;var t,e,i,n;this._input||(this.done=!0),this._more||(this.yytext="",this.match="");for(var r=this._currentRules(),s=0;s<r.length;s++)if((i=this._input.match(this.rules[r[s]]))&&(!e||i[0].length>e[0].length)){if(e=i,n=s,this.options.backtrack_lexer){if(!1!==(t=this.test_match(i,r[s])))return t;if(this._backtrack){e=!1;continue}return!1}if(!this.options.flex)break}return e?!1!==(t=this.test_match(e,r[n]))&&t:""===this._input?this.EOF:this.parseError("Lexical error on line "+(this.yylineno+1)+". Unrecognized text.\n"+this.showPosition(),{text:"",token:null,line:this.yylineno})}),"next"),lex:t((function(){var t=this.next();return t||this.lex()}),"lex"),begin:t((function(t){this.conditionStack.push(t)}),"begin"),popState:t((function(){return this.conditionStack.length-1>0?this.conditionStack.pop():this.conditionStack[0]}),"popState"),_currentRules:t((function(){return this.conditionStack.length&&this.conditionStack[this.conditionStack.length-1]?this.conditions[this.conditionStack[this.conditionStack.length-1]].rules:this.conditions.INITIAL.rules}),"_currentRules"),topState:t((function(t){return(t=this.conditionStack.length-1-Math.abs(t||0))>=0?this.conditionStack[t]:"INITIAL"}),"topState"),pushState:t((function(t){this.begin(t)}),"pushState"),stateStackSize:t((function(){return this.conditionStack.length}),"stateStackSize"),options:{"case-insensitive":!0},performAction:t((function(t,e,i,n){switch(i){case 0:return"title";case 1:return this.begin("acc_title"),9;case 2:return this.popState(),"acc_title_value";case 3:return this.begin("acc_descr"),11;case 4:return this.popState(),"acc_descr_value";case 5:this.begin("acc_descr_multiline");break;case 6:case 48:this.popState();break;case 7:return"acc_descr_multiline_value";case 8:return 5;case 9:case 10:case 11:break;case 12:return 8;case 13:return 6;case 14:return 19;case 15:return 30;case 16:return 22;case 17:return 21;case 18:return 24;case 19:return 26;case 20:return 28;case 21:return 31;case 22:return 32;case 23:return 33;case 24:return 34;case 25:return 35;case 26:return 36;case 27:return 37;case 28:return 38;case 29:return 39;case 30:return 40;case 31:return 41;case 32:return 42;case 33:return 43;case 34:return 44;case 35:return 55;case 36:return 56;case 37:return 57;case 38:return 58;case 39:return 59;case 40:return 60;case 41:return 61;case 42:return 47;case 43:return 49;case 44:return 51;case 45:return 54;case 46:return 53;case 47:this.begin("string");break;case 49:return"qString";case 50:return e.yytext=e.yytext.trim(),62}}),"anonymous"),rules:[/^(?:title\s[^#\n;]+)/i,/^(?:accTitle\s*:\s*)/i,/^(?:(?!\n||)*[^\n]*)/i,/^(?:accDescr\s*:\s*)/i,/^(?:(?!\n||)*[^\n]*)/i,/^(?:accDescr\s*\{\s*)/i,/^(?:[\}])/i,/^(?:[^\}]*)/i,/^(?:(\r?\n)+)/i,/^(?:\s+)/i,/^(?:#[^\n]*)/i,/^(?:%[^\n]*)/i,/^(?:$)/i,/^(?:requirementDiagram\b)/i,/^(?:\{)/i,/^(?:\})/i,/^(?::)/i,/^(?:id\b)/i,/^(?:text\b)/i,/^(?:risk\b)/i,/^(?:verifyMethod\b)/i,/^(?:requirement\b)/i,/^(?:functionalRequirement\b)/i,/^(?:interfaceRequirement\b)/i,/^(?:performanceRequirement\b)/i,/^(?:physicalRequirement\b)/i,/^(?:designConstraint\b)/i,/^(?:low\b)/i,/^(?:medium\b)/i,/^(?:high\b)/i,/^(?:analysis\b)/i,/^(?:demonstration\b)/i,/^(?:inspection\b)/i,/^(?:test\b)/i,/^(?:element\b)/i,/^(?:contains\b)/i,/^(?:copies\b)/i,/^(?:derives\b)/i,/^(?:satisfies\b)/i,/^(?:verifies\b)/i,/^(?:refines\b)/i,/^(?:traces\b)/i,/^(?:type\b)/i,/^(?:docref\b)/i,/^(?:<-)/i,/^(?:->)/i,/^(?:-)/i,/^(?:["])/i,/^(?:["])/i,/^(?:[^"]*)/i,/^(?:[\w][^\r\n\{\<\>\-\=]*)/i],conditions:{acc_descr_multiline:{rules:[6,7],inclusive:!1},acc_descr:{rules:[4],inclusive:!1},acc_title:{rules:[2],inclusive:!1},unqString:{rules:[],inclusive:!1},token:{rules:[],inclusive:!1},string:{rules:[48,49],inclusive:!1},INITIAL:{rules:[0,1,3,5,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50],inclusive:!0}}}}();function U(){this.yy={}}return P.lexer=V,t(U,"Parser"),U.prototype=P,P.Parser=U,new U}();y.parser=y;var _=y,g=[],E={},m=new Map,R={},f=new Map,I=t(((t,e)=>(m.has(t)||m.set(t,{name:t,type:e,id:E.id,text:E.text,risk:E.risk,verifyMethod:E.verifyMethod}),E={},m.get(t))),"addRequirement"),S=t((()=>m),"getRequirements"),b=t((t=>{void 0!==E&&(E.id=t)}),"setNewReqId"),N=t((t=>{void 0!==E&&(E.text=t)}),"setNewReqText"),T=t((t=>{void 0!==E&&(E.risk=t)}),"setNewReqRisk"),k=t((t=>{void 0!==E&&(E.verifyMethod=t)}),"setNewReqVerifyMethod"),x=t((t=>(f.has(t)||(f.set(t,{name:t,type:R.type,docRef:R.docRef}),l.info("Added new requirement: ",t)),R={},f.get(t))),"addElement"),A=t((()=>f),"getElements"),w=t((t=>{void 0!==R&&(R.type=t)}),"setNewElementType"),q=t((t=>{void 0!==R&&(R.docRef=t)}),"setNewElementDocRef"),v=t(((t,e,i)=>{g.push({type:t,src:e,dst:i})}),"addRelationship"),$=t((()=>g),"getRelationships"),O=t((()=>{g=[],E={},m=new Map,R={},f=new Map,o()}),"clear"),L={RequirementType:{REQUIREMENT:"Requirement",FUNCTIONAL_REQUIREMENT:"Functional Requirement",INTERFACE_REQUIREMENT:"Interface Requirement",PERFORMANCE_REQUIREMENT:"Performance Requirement",PHYSICAL_REQUIREMENT:"Physical Requirement",DESIGN_CONSTRAINT:"Design Constraint"},RiskLevel:{LOW_RISK:"Low",MED_RISK:"Medium",HIGH_RISK:"High"},VerifyType:{VERIFY_ANALYSIS:"Analysis",VERIFY_DEMONSTRATION:"Demonstration",VERIFY_INSPECTION:"Inspection",VERIFY_TEST:"Test"},Relationships:{CONTAINS:"contains",COPIES:"copies",DERIVES:"derives",SATISFIES:"satisfies",VERIFIES:"verifies",REFINES:"refines",TRACES:"traces"},getConfig:t((()=>s().req),"getConfig"),addRequirement:I,getRequirements:S,setNewReqId:b,setNewReqText:N,setNewReqRisk:T,setNewReqVerifyMethod:k,setAccTitle:r,getAccTitle:n,setAccDescription:i,getAccDescription:e,addElement:x,getElements:A,setNewElementType:w,setNewElementDocRef:q,addRelationship:v,getRelationships:$,clear:O},C=t((t=>`\n\n  marker {\n    fill: ${t.relationColor};\n    stroke: ${t.relationColor};\n  }\n\n  marker.cross {\n    stroke: ${t.lineColor};\n  }\n\n  svg {\n    font-family: ${t.fontFamily};\n    font-size: ${t.fontSize};\n  }\n\n  .reqBox {\n    fill: ${t.requirementBackground};\n    fill-opacity: 1.0;\n    stroke: ${t.requirementBorderColor};\n    stroke-width: ${t.requirementBorderSize};\n  }\n  \n  .reqTitle, .reqLabel{\n    fill:  ${t.requirementTextColor};\n  }\n  .reqLabelBox {\n    fill: ${t.relationLabelBackground};\n    fill-opacity: 1.0;\n  }\n\n  .req-title-line {\n    stroke: ${t.requirementBorderColor};\n    stroke-width: ${t.requirementBorderSize};\n  }\n  .relationshipLine {\n    stroke: ${t.relationColor};\n    stroke-width: 1;\n  }\n  .relationshipLabel {\n    fill: ${t.relationLabelColor};\n  }\n\n`),"getStyles"),M={CONTAINS:"contains",ARROW:"arrow"},F={ReqMarkers:M,insertLineEndings:t(((t,e)=>{let i=t.append("defs").append("marker").attr("id",M.CONTAINS+"_line_ending").attr("refX",0).attr("refY",e.line_height/2).attr("markerWidth",e.line_height).attr("markerHeight",e.line_height).attr("orient","auto").append("g");i.append("circle").attr("cx",e.line_height/2).attr("cy",e.line_height/2).attr("r",e.line_height/2).attr("fill","none"),i.append("line").attr("x1",0).attr("x2",e.line_height).attr("y1",e.line_height/2).attr("y2",e.line_height/2).attr("stroke-width",1),i.append("line").attr("y1",0).attr("y2",e.line_height).attr("x1",e.line_height/2).attr("x2",e.line_height/2).attr("stroke-width",1),t.append("defs").append("marker").attr("id",M.ARROW+"_line_ending").attr("refX",e.line_height).attr("refY",.5*e.line_height).attr("markerWidth",e.line_height).attr("markerHeight",e.line_height).attr("orient","auto").append("path").attr("d",`M0,0\n      L${e.line_height},${e.line_height/2}\n      M${e.line_height},${e.line_height/2}\n      L0,${e.line_height}`).attr("stroke-width",1)}),"insertLineEndings")},D={},P=0,V=t(((t,e)=>t.insert("rect","#"+e).attr("class","req reqBox").attr("x",0).attr("y",0).attr("width",D.rect_min_width+"px").attr("height",D.rect_min_height+"px")),"newRectNode"),U=t(((t,e,i)=>{let n=D.rect_min_width/2,r=t.append("text").attr("class","req reqLabel reqTitle").attr("id",e).attr("x",n).attr("y",D.rect_padding).attr("dominant-baseline","hanging"),s=0;i.forEach((t=>{0==s?r.append("tspan").attr("text-anchor","middle").attr("x",D.rect_min_width/2).attr("dy",0).text(t):r.append("tspan").attr("text-anchor","middle").attr("x",D.rect_min_width/2).attr("dy",.75*D.line_height).text(t),s++}));let a=1.5*D.rect_padding+s*D.line_height*.75;return t.append("line").attr("class","req-title-line").attr("x1","0").attr("x2",D.rect_min_width).attr("y1",a).attr("y2",a),{titleNode:r,y:a}}),"newTitleNode"),Y=t(((t,e,i,n)=>{let r=t.append("text").attr("class","req reqLabel").attr("id",e).attr("x",D.rect_padding).attr("y",n).attr("dominant-baseline","hanging"),s=0;let a=[];return i.forEach((t=>{let e=t.length;for(;e>30&&s<3;){let i=t.substring(0,30);e=(t=t.substring(30,t.length)).length,a[a.length]=i,s++}if(3==s){let t=a[a.length-1];a[a.length-1]=t.substring(0,t.length-4)+"..."}else a[a.length]=t;s=0})),a.forEach((t=>{r.append("tspan").attr("x",D.rect_padding).attr("dy",D.line_height).text(t)})),r}),"newBodyNode"),B=t(((t,e,i,n)=>{const r=e.node().getTotalLength(),s=e.node().getPointAtLength(.5*r),a="rel"+P;P++;const o=t.append("text").attr("class","req relationshipLabel").attr("id",a).attr("x",s.x).attr("y",s.y).attr("text-anchor","middle").attr("dominant-baseline","middle").text(n).node().getBBox();t.insert("rect","#"+a).attr("class","req reqLabelBox").attr("x",s.x-o.width/2).attr("y",s.y-o.height/2).attr("width",o.width).attr("height",o.height).attr("fill","white").attr("fill-opacity","85%")}),"addEdgeLabel"),j=t((function(t,e,i,n,r){const s=i.edge(G(e.src),G(e.dst)),a=p().x((function(t){return t.x})).y((function(t){return t.y})),o=t.insert("path","#"+n).attr("class","er relationshipLine").attr("d",a(s.points)).attr("fill","none");e.type==r.db.Relationships.CONTAINS?o.attr("marker-start","url("+h.getUrl(D.arrowMarkerAbsolute)+"#"+e.type+"_line_ending)"):(o.attr("stroke-dasharray","10,7"),o.attr("marker-end","url("+h.getUrl(D.arrowMarkerAbsolute)+"#"+F.ReqMarkers.ARROW+"_line_ending)")),B(t,o,D,`<<${e.type}>>`)}),"drawRelationshipFromLayout"),Q=t(((t,e,i)=>{t.forEach(((t,n)=>{n=G(n),l.info("Added new requirement: ",n);const r=i.append("g").attr("id",n),s=V(r,"req-"+n);let a=[],o=U(r,n+"_title",[`<<${t.type}>>`,`${t.name}`]);a.push(o.titleNode);let h=Y(r,n+"_body",[`Id: ${t.id}`,`Text: ${t.text}`,`Risk: ${t.risk}`,`Verification: ${t.verifyMethod}`],o.y);a.push(h);const c=s.node().getBBox();e.setNode(n,{width:c.width,height:c.height,shape:"rect",id:n})}))}),"drawReqs"),H=t(((t,e,i)=>{t.forEach(((t,n)=>{const r=G(n),s=i.append("g").attr("id",r),a="element-"+r,o=V(s,a);let l=[],h=U(s,a+"_title",["<<Element>>",`${n}`]);l.push(h.titleNode);let c=Y(s,a+"_body",[`Type: ${t.type||"Not Specified"}`,`Doc Ref: ${t.docRef||"None"}`],h.y);l.push(c);const u=o.node().getBBox();e.setNode(r,{width:u.width,height:u.height,shape:"rect",id:r})}))}),"drawElements"),W=t(((t,e)=>(t.forEach((function(t){let i=G(t.src),n=G(t.dst);e.setEdge(i,n,{relationship:t})})),t)),"addRelationships"),K=t((function(t,e){e.nodes().forEach((function(i){void 0!==i&&void 0!==e.node(i)&&(t.select("#"+i),t.select("#"+i).attr("transform","translate("+(e.node(i).x-e.node(i).width/2)+","+(e.node(i).y-e.node(i).height/2)+" )"))}))}),"adjustEntities"),G=t((t=>t.replace(/\s/g,"").replace(/\./g,"_")),"elementString"),z={parser:_,db:L,renderer:{draw:t(((t,e,i,n)=>{const r=(D=s().requirement).securityLevel;let o;"sandbox"===r&&(o=c("#i"+e));const l=c("sandbox"===r?o.nodes()[0].contentDocument.body:"body").select(`[id='${e}']`);F.insertLineEndings(l,D);const h=new u({multigraph:!1,compound:!1,directed:!0}).setGraph({rankdir:D.layoutDirection,marginx:20,marginy:20,nodesep:100,edgesep:100,ranksep:100}).setDefaultEdgeLabel((function(){return{}}));let p=n.db.getRequirements(),y=n.db.getElements(),_=n.db.getRelationships();Q(p,h,l),H(y,h,l),W(_,h),d(h),K(l,h),_.forEach((function(t){j(l,t,h,e,n)}));const g=D.rect_padding,E=l.node().getBBox(),m=E.width+2*g,R=E.height+2*g;a(l,R,m,D.useMaxWidth),l.attr("viewBox",`${E.x-g} ${E.y-g} ${m} ${R}`)}),"draw")},styles:C};export{z as diagram};
