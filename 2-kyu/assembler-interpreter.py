import re


def assembler_interpreter(program):
    p = 0
    cmp = (0,0)
    cmds, funcs = clear_input(program)
    a = call_func(cmds, {}, funcs, cmds)

    return output if a else -1

def clear_input(program):
    program = [re.sub(';(.*)','',re.sub('\s{2,}',' ',x)) for x in  program.split('\n')]
    program = [x for x in program if len(x)>2]
    funcs = {}
    clean_program = []
    curr_func = ''

    for cmd in program:
        if cmd[-1] == ':':
            funcs[cmd[:-1]] = []
            curr_func = cmd[:-1]
            continue
        if cmd[0] != cmd[0].lstrip():
            funcs[curr_func].append(cmd[1:])
        else:
            clean_program.append(cmd)

    return (clean_program, funcs)

def call_func(cmds, register, funcs, pr, last_pointer=0, start=0):
    p = start
    while p < len(cmds):
        if cmds[p][:3]!='msg':
            cmd, a1, a2 = (cmds[p].replace(',','') + ' 0' + ' 0' + ' 0').split()[:3]
            if   cmd=='mov': register[a1] = register[a2] if a2.isalpha() else int(a2)
            elif cmd=='inc': register[a1]+=1
            elif cmd=='dec': register[a1]-=1
            elif cmd=='add': register[a1]+=(int(a2) if a2.isdigit() else register[a2])
            elif cmd=='sub': register[a1]-=(int(a2) if a2.isdigit() else register[a2])
            elif cmd=='mul': register[a1]*=(int(a2) if a2.isdigit() else register[a2])
            elif cmd=='div': register[a1]//=(int(a2) if a2.isdigit() else register[a2])
            elif cmd=='jmp': return call_func(funcs[a1], register, funcs, pr, last_pointer)
            elif cmd=='call':return call_func(funcs[a1], register, funcs, pr, p)
            elif cmd=='cmp':
                cmp = (int(a1) if a1.isdigit() else register[a1], int(a2) if a2.isdigit() else register[a2])
            elif cmd=='jne':
                if cmp[0]!=cmp[1]: return call_func(funcs[a1], register, funcs, pr, last_pointer)
            elif cmd=='je':
                if cmp[0]==cmp[1]: return call_func(funcs[a1], register, funcs, pr, last_pointer)
            elif cmd=='jge':
                if cmp[0]>=cmp[1]: return call_func(funcs[a1], register, funcs, pr, last_pointer)
            elif cmd=='jg':
                if cmp[0]>cmp[1]:  return call_func(funcs[a1], register, funcs, pr, last_pointer)
            elif cmd=='jle':
                if cmp[0]<=cmp[1]: return call_func(funcs[a1], register, funcs, pr, last_pointer)
            elif cmd=='jl':
                if cmp[0]<cmp[1]:  return call_func(funcs[a1], register, funcs, pr, last_pointer)
            elif cmd=='ret':
                return call_func(pr, register, funcs, pr, last_pointer, last_pointer+1)
            elif cmd=='end':
                return 1

        else:
            clean_str = re.sub("[a-z]\,\s\'", '*', re.sub("\'\,\s[a-z]", 'z', cmds[p])).replace("'", "")
            clean_str = re.sub("\s[z]", ' *', clean_str)
            comp = re.compile("\'\,\s[a-z]|[a-z]\,")
            s_vars = [x.replace("'", "").replace(",", "").replace(" ","") for x in comp.findall(cmds[p])]

            ms, iter = '', 0

            for x in (clean_str):
              if x == '*':
                ms+=str(register[s_vars[iter]])
                iter+=1
              else:
                ms+=x

            global output
            output = ms[4:].strip()

        p+=1

'''
This is the second part of this kata series. First part is here.

We want to create an interpreter of assembler which will support the following instructions:

    mov x, y - copy y (either an integer or the value of a register) into register x.
    inc x - increase the content of register x by one.
    dec x - decrease the content of register x by one.
    add x, y - add the content of the register x with y (either an integer or the value of a register)
     and stores the result in x (i.e. register[x] += y).
    sub x, y - subtract y (either an integer or the value of a register) from the register x and stores
     the result in x (i.e. register[x] -= y).
    mul x, y - same with multiply (i.e. register[x] *= y).
    div x, y - same with integer division (i.e. register[x] /= y).
    label: - define a label position (label = identifier + ":", an identifier being a string that does
     not match any other command). Jump commands and call are aimed to these labels positions in the program.
    jmp lbl - jumps to to the label lbl.
    cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value
     of a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
    jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
    je lbl - jump to the label lbl if the values of the previous cmp command were equal.
    jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
    jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
    jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
    jl lbl - jump to the label lbl if x was less than y in the previous cmp command.
    call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction
     pointer should return to the instruction next to this call command.
    ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that
     called the current function.
    msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings
     (delimited by single quotes) and registers. The number of arguments isn't limited and will vary,
      depending on the program.
    end - this instruction indicates that the program ends correctly, so the stored output is returned
     (if the program terminates without this instruction it should return the default output: see below).
    ; comment - comments should not be taken in consideration during the execution of the program.


Output format:

The normal output format is a string (returned with the end command).

If the program does finish itself without using an end instruction, the default return value is:

-1 (as an integer)


Input format:

The function/method will take as input a multiline string of instructions, delimited with EOL characters.
 Please, note that the instructions may also have indentation for readability purposes.

For example:

program = """
; My first program
mov  a, 5
inc  a
call function
msg  '(5+1)/2 = ', a    ; output message
end

function:
    div  a, 2
    ret
"""
assembler_interpreter(program)

The above code would set register a to 5, increase its value by 1, calls the subroutine function,
 divide its value by 2, returns to the first call instruction, prepares the output of the program and
  then returns it with the end instruction. In this case, the output would be (5+1)/2 = 3.

'''
