Title: conda 的基本使用
Date: 2017-10-15 00:03:43
Category: Tools
Tags: conda, Tools

* 帮助

```bash
conda help COMMAND
```

* 常用命令

| Task | Command |
| :-: | :-: |
| Install a package | `conda install $PACKAGE_NAME` |
| Update a package | `conda update --name $ENVIRONMENT_NAME $PACKAGE_NAME` |
| Update package manager | `conda update conda` |
| Uninstall a package | `conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME` |
| Create an environment | `conda create --name $ENVIRONMENT_NAME python` |
| Activate an environment | `source activate $ENVIRONMENT_NAME` |
| Deactivate an environment | `source deactivate` |
| Search available packages | `conda search $SEARCH_TERM` |
| Install package from specific source | `conda install --channel $URL $PACKAGE_NAME` |
| List installed packages | `conda list --name $ENVIRONMENT_NAME` |
| Create requirements file | `conda list --export` |
| List all environments | `conda info --envs` |
| Install other package manager | `conda install pip` |
| Install Python | `conda install python=x.x` |
| Update Python | `conda update python` |



