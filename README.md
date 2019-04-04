### 说明

这是一个Ansible Python Api的封装。

### 安装

```bash
$ python setup.py install
```

### 简单使用

```python
from Asi import Api


if __name__ == "__main__":
	hosts = [
		{
			"hostname": "localhost",
			"port": 22,
			"vars": {
				"ansible_ssh_user": "root",
				"ansible_ssh_pass": "p@ssw0rd"
			}
		},
		{
			"hostname": "192.168.152.142",
			"port": 22,
			"vars": {
				"ansible_ssh_user": "root",
				"ansible_ssh_pass": "p@ssw0rd"
			}
		}
	]

	Api().module("shell", args="ls", register='shell_out', task_name="test")\
		 .module("debug", args={"msg":"{{shell_out.stdout}}"})\
		 .run(hosts)	
```
