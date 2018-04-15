# vision-comp

## Workstation
 - 1 Install pipenv
 - 2.1 Add in .bashrc
 - 2.2 Add in .zshrc

### 1 Install pipenv
```bash
pip install --user pipenv
```

#### 2.1 Add in .bashrc
```bash
## local_user: pipenv and others binary
if [[ -d $HOME/.local ]]; then
    export LOCAL_USER="$HOME/.local"
    export PATH="$LOCAL_USER/bin:$PATH"
fi

if command -v pipenv &> /dev/null; then
    eval "$(pipenv --completion)"
fi

if command -v pip &> /dev/null; then
    eval "$(pip completion --zsh)"
fi
```

#### 2.2 Add in .zshrc
```zsh
## local_user: pipenv and others binary
if [[ -d $HOME/.local ]]; then
    export LOCAL_USER="$HOME/.local"
    export PATH="$LOCAL_USER/bin:$PATH"
fi

if (( $+commands[pipenv] )); then
    eval "$(pipenv --completion)"
fi

if (( $+commands[pip] )); then
    eval "$(pip completion --zsh)"
fi
```

## aulas
 - Visão computacional
 - Processamento de imagens
