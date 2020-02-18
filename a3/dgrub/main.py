#!/bin/python3
import json #Used to load json
from jinja2 import Environment, FileSystemLoader #Templating

def main(args):
    e = Environment(loader=FileSystemLoader('templates/'))
    linux_template = e.get_template("linux.tmpl")
    netboot_template = e.get_template("netboot.tmpl")

    with open('./entries.json') as json_file:
        custom_grub_data = json.load(json_file)

    netboot = netboot_template.render(title='"'+custom_grub_data[0]["title"]+'"',
                                      kernel_path=custom_grub_data[0]["kernel_path"])

    custom_initrd = linux_template.render(title='"'+custom_grub_data[1]["title"]+'"',
                                    top=custom_grub_data[1]["top"][0],
                                    kernel_path=custom_grub_data[1]["kernel_path"],
                                    kernel_arg_1=custom_grub_data[1]["kernel_args"][0],
                                    kernel_arg_2=custom_grub_data[1]["kernel_args"][1],
                                    kernel_arg_3=custom_grub_data[1]["kernel_args"][2],
                                    initrd_path=custom_grub_data[1]["initrd_path"])

    xubuntu = linux_template.render(title='"'+custom_grub_data[2]["title"]+'"',
                                    top=custom_grub_data[2]["top"][0] + "\n  " + custom_grub_data[2]["top"][1],
                                    kernel_path=custom_grub_data[2]["kernel_path"],
                                    kernel_arg_1=custom_grub_data[2]["kernel_args"][0],
                                    kernel_arg_2=custom_grub_data[2]["kernel_args"][1],
                                    kernel_arg_3=custom_grub_data[2]["kernel_args"][2],
                                    initrd_path=custom_grub_data[2]["initrd_path"])

    print("The following entries will be appended to the '/etc/grub.d/40_custom'")
    print(netboot)
    print(custom_initrd)
    print(xubuntu)

    with open("/etc/grub.d/40_custom", 'a') as output_file:
        output_file.write(netboot)
        output_file.write(custom_initrd)
        output_file.write(xubuntu)

if __name__ == "__main__":
    args = None
    main(args)

