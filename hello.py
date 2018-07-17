import ptvsd

# Allow other computers to attach to ptvsd at this IP address and port, using the secret
ptvsd.enable_attach("my_secret", address = ('1.2.3.4', 3000))

# Pause the program until a remote debugger is attached
ptvsd.wait_for_attach()

import torch
print('hello world2')
print(torch.cuda.is_available())
print('hello world')