"set background=dark

" use indentation of previous line
set autoindent
" use intelligent indentation for C
set smartindent

" do not wrap line
" set nowrap

" allways show status line
set ls=2
set statusline=%<[%n][%f]%m%r%h%w%{'['.(&fenc!=''?&fenc:&enc).':'.&ff.']'}%y\ [POS=%05l,%05v][%p%%]

"line number
"set nu

" make backspace a more flexible
set backspace=indent,eol,start 

" Use the below highlight group when displaying bad whitespace is desired
highlight BadWhitespace ctermbg=red guibg=red
set cursorline
hi CursorLine cterm=bold

syntax on

au BufNewFile,BufRead *.mi set filetype=perl
au BufNewFile,BufRead *.m set filetype=perl
" load filetype plugins/indent settings
filetype plugin indent on
" expand tabs to spaces
au BufRead,BufNewFile *.sh,*.rb,*.py,*.pyw,*.c,*.h,*.cpp,*.s,*.S,*.html,*.htm,*.pl,*.pm,*.mi,*.m,*.js,*.java,*.xml,*.xsd,*.wsdl,*.asdl,*.scala set expandtab
au BufRead,BufNewFile Makefile* set noexpandtab
au BufRead,BufNewFile *.xml set noexpandtab
" how many spaces for indenting
set shiftwidth=3
" tab width_
set tabstop=3

autocmd BufRead,BufNewFile *.scala set shiftwidth=2
autocmd BufRead,BufNewFile *.scala set tabstop=2
autocmd BufRead,BufNewFile *.scala set softtabstop=2
autocmd BufRead,BufNewFile *.java set shiftwidth=2
autocmd BufRead,BufNewFile *.java  set tabstop=2
autocmd BufRead,BufNewFile *.java set softtabstop=2
autocmd BufRead,BufNewFile *.m set shiftwidth=2
autocmd BufRead,BufNewFile *.m  set tabstop=2
autocmd BufRead,BufNewFile *.m set softtabstop=2
autocmd BufRead,BufNewFile *.mi set shiftwidth=2
autocmd BufRead,BufNewFile *.mi set tabstop=2
autocmd BufRead,BufNewFile *.mi set softtabstop=2
autocmd BufRead,BufNewFile *.pl set shiftwidth=2
autocmd BufRead,BufNewFile *.pl set tabstop=2
autocmd BufRead,BufNewFile *.pl set softtabstop=2
autocmd BufRead,BufNewFile *.pm set shiftwidth=2
autocmd BufRead,BufNewFile *.pm set tabstop=2
autocmd BufRead,BufNewFile *.pm set softtabstop=2
autocmd BufRead,BufNewFile *.html set shiftwidth=2
autocmd BufRead,BufNewFile *.html set tabstop=2
autocmd BufRead,BufNewFile *.html set softtabstop=2
autocmd BufRead,BufNewFile *.rb set shiftwidth=2
autocmd BufRead,BufNewFile *.rb set tabstop=2
autocmd BufRead,BufNewFile *.rb set softtabstop=2
autocmd BufRead,BufNewFile *.sh set shiftwidth=2
autocmd BufRead,BufNewFile *.sh set tabstop=2
autocmd BufRead,BufNewFile *.sh set softtabstop=2
autocmd BufRead,BufNewFile *.js set shiftwidth=2
autocmd BufRead,BufNewFile *.js set tabstop=2
autocmd BufRead,BufNewFile *.js set softtabstop=2

" Use UNIX (\n) line endings.
" Only used for new files so as to not force existing files to change their
" line endings.
au BufNewFile * set fileformat=unix

set fileformat=unix

" give cursor position
"set ruler
" number of undos
set undolevels=2000

" jump to the word you search during you type
set incsearch
set ignorecase
" highligth search results
set hlsearch
" continue searching at top when hitting bottom
"set wrapscan
" backup into ~/.vmm/backup
set backup
set backupdir=~/.vim/backup

" fuck the beeps
set noerrorbells



" display utf-8 chars
set encoding=utf-8
set enc=utf-8
set fenc=utf-8
set termencoding=utf-8


" use , as mapleader variable
let mapleader=","



" comment types_
set comments=b:#,:%,fb:-,n:),n:> fo=cqrt


iab packet paket
iab Packet Paket
iab felher fehler
iab paranoit paranoid
iab Standart Standard
iab herran hera
iab ider oder
iab alos also
iab charcter character
iab examlpe example
iab nciht nicht
iab Netwokr     Network
iab Srever      Server
iab Standart    Standard
iab standart    standard
iab SIe         Sie
iab ICh         Ich
iab cih         ich
iab shc         sch
iab amchen      machen
iab amche       mache
iab Linx        Linux

" give current date
iab DATE <C-R>=strftime("%a %b %d %T %Z %Y")<CR>




" before quit vim, save editing session
" Tell vim to remember certain things when we exit
"  '10  :  marks will be remembered for up to 10 previously edited files
"  "100 :  will save up to 100 lines for each register
"  :20  :  up to 20 lines of command-line history will be remembered
"  %    :  saves and restores the buffer list
"  n... :  where to save the viminfo files
set viminfo='10,\"100,:20,%,n~/.viminfo

function! ResCur()
  if line("'\"") <= line("$")
    normal! g`"
    return 1
  endif
endfunction

" Restore cursor to file position in previous editing session
augroup resCur
  autocmd!
  autocmd BufWinEnter * call ResCur()
augroup END





" ==============================================
" Mappings
" ==============================================
" use shell with ctrl-z
map <C-Z> :shell


" line numbering
map <LEADER>ln :%s/^/\=line('.')/<CR><ESC>

" add a comment
map ,c i/*  */<Left><Left><Left>


" use pon and poff instead of set no/paste
map <Leader>pon  :set paste<CR>$
imap <Leader>pon  <Esc>:set paste<CR>a$
map <Leader>poff :set nopaste<CR>$
imap <Leader>poff <Esc>:set nopaste<CR>a$


" convert text2html
map ,w :runtime! syntax/2html.vim
"spelling check
map <F2> :set spelllang=en<CR>:set spell!<CR><Bar>:echo "Spell Check: " . strpart("OffOn", 3 * &spell, 3)<CR>
set modeline
