.LFB0:
        .cfi_startproc
        push    rbp                        
        .cfi_def_cfa_offset 16
        .cfi_offset 6, -16
        mov     rbp, rsp                   
        .cfi_def_cfa_register 6

        mov     DWORD PTR -96[rbp], 88     
        mov     DWORD PTR -92[rbp], 83      
        mov     DWORD PTR -88[rbp], 72      
        mov     DWORD PTR -84[rbp], 89     
        mov     DWORD PTR -80[rbp], 75   
        mov     DWORD PTR -76[rbp], 118      
        mov     DWORD PTR -72[rbp], 83     
        mov     DWORD PTR -68[rbp], 111     
        mov     DWORD PTR -64[rbp], 106      
        mov     DWORD PTR -60[rbp], 112     
        mov     DWORD PTR -56[rbp], 112     
        mov     DWORD PTR -52[rbp], 108    
        mov     DWORD PTR -48[rbp], 99    
        mov     DWORD PTR -44[rbp], 93     
        mov     DWORD PTR -40[rbp], 114     
        mov     DWORD PTR -36[rbp], 113      
        mov     DWORD PTR -32[rbp], 119      
        mov     DWORD PTR -28[rbp], 116     
        mov     DWORD PTR -24[rbp], 112      
        mov     DWORD PTR -20[rbp], 103    
        mov     DWORD PTR -16[rbp], 79      
        mov     DWORD PTR -12[rbp], 116     
        mov     DWORD PTR -4[rbp], 0        

        jmp     .L2                        
.L3:
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     eax, DWORD PTR -96[rbp+rax*4]  
        lea     edx, -5[rax]                
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     DWORD PTR -96[rbp+rax*4], edx  
        add     DWORD PTR -4[rbp], 1        
.L2:
        cmp     DWORD PTR -4[rbp], 4        
        jle     .L3                         

        mov     DWORD PTR -4[rbp], 5        
        jmp     .L4                         
.L5:
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     eax, DWORD PTR -96[rbp+rax*4]  
        lea     edx, 5[rax]                 
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     DWORD PTR -96[rbp+rax*4], edx  
        add     DWORD PTR -4[rbp], 1        
.L4:
        cmp     DWORD PTR -4[rbp], 9        
        jle     .L5                         

        mov     DWORD PTR -4[rbp], 10       
        jmp     .L6                         
.L7:
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     eax, DWORD PTR -96[rbp+rax*4]  
        lea     edx, 2[rax]                 
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     DWORD PTR -96[rbp+rax*4], edx  
        add     DWORD PTR -4[rbp], 1        
.L6:
        cmp     DWORD PTR -4[rbp], 14       
        jle     .L7                         

        mov     DWORD PTR -4[rbp], 15       
        jmp     .L8                         
.L9:
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     eax, DWORD PTR -96[rbp+rax*4]  
        lea     edx, -2[rax]                
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     DWORD PTR -96[rbp+rax*4], edx  
        add     DWORD PTR -4[rbp], 1        
.L8:
        cmp     DWORD PTR -4[rbp], 19       
        jle     .L9                         

        mov     DWORD PTR -4[rbp], 20       
        jmp     .L10                        
.L11:
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     eax, DWORD PTR -96[rbp+rax*4]  
        lea     edx, 9[rax]                 
        mov     eax, DWORD PTR -4[rbp]      
        cdqe                                
        mov     DWORD PTR -96[rbp+rax*4], edx  
        add     DWORD PTR -4[rbp], 1        
.L10:
        cmp     DWORD PTR -4[rbp], 21       
        jle     .L11                        

        mov     eax, 0                      
        pop     rbp                         
        .cfi_def_cfa 7, 8
        ret                                 
        .cfi_endproc
.LFE0:
        .size   main, .-main
        .section        .note.GNU-stack,"",@progbits
