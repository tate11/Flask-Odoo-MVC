import os,sys,argparse
import data


# Globals
#-------------------------------------------------------------------
#-------------------------------------------------------------------

dirs=['config','controllers','models','forms','app_config',
		'static','templates','i18n','doc','data']


files=['__init__.py','config.py','models.py','forms.py',
	  'app_config.py','controller.py','main_app.py','README.md','run_app.sh','requirements.txt']

# Methods
#-------------------------------------------------------------------
#-------------------------------------------------------------------




# Create the files and custom code entries
#-------------------------------------------------------------------
def create_project_files(project_name=""):

	parent_folder=project_name
	os.mkdir(parent_folder)
	print("")
	print("		PROJECT: %s" % parent_folder.capitalize())
	print("---------------------------------")
	print("		|\n		|")

	for dire in dirs:
		project_name_folder=parent_folder+"/"+dire
		print("		|____",dire)
		print("		|")
		if dire == 'config':
			os.mkdir(project_name_folder)
			fp=open(project_name_folder+"/"+files[0],"w")
			fp.writelines(data.init_config_data)
			fp.close()
			print("			|___ __init__.py")
			print("		|")
			fp=open(project_name_folder+"/"+files[1],"w")
			fp.writelines(data.config_data)
			fp.close()
			print("			|___ config.py")
			print("		|")

		elif dire == "models":
			os.mkdir(project_name_folder)
			fp=open(project_name_folder+"/"+files[0],"w")
			fp.writelines(data.init_models_data)
			fp.close()
			print("			|___ __init__.py")
			print("		|")

			fp=open(project_name_folder+"/"+files[2],"w")
			fp.writelines(data.models_data)
			fp.close()
			print("			|___ models.py")
			print("		|")

		elif dire == "forms":
			os.mkdir(project_name_folder)
			fp=open(project_name_folder+"/"+files[0],"w")
			fp.writelines(data.init_forms_data)
			fp.close()
			print("			|___ __init__.py")
			print("		|")

			fp=open(project_name_folder+"/"+files[3],"w")
			fp.writelines(data.forms_data)
			fp.close()
			print("			|___ forms.py")
			print("		|")

		elif dire == "app_config":
			os.mkdir(project_name_folder)
			fp=open(project_name_folder+"/"+files[0],"w")
			fp.writelines(data.init_app_config)
			fp.close()
			print("			|___ __init__.py")
			print("		|")
			fp=open(project_name_folder+"/"+files[4],"w")
			fp.writelines(data.app_config_data)
			fp.close()
			print("			|___ app_config.py")
			print("		|")

		elif dire == "controllers":
			os.mkdir(project_name_folder)
			fp=open(project_name_folder+"/"+files[0],"w")
			fp.writelines(data.init_controllers_data)
			fp.close()
			print("			|___ __init__.py")
			print("		|")

			fp=open(project_name_folder+"/"+files[5],"w")
			fp.writelines(data.controllers_data)
			fp.close()
			print("			|___ controllers.py")
			print("		|")

		else:
			if dire=="doc":
				print("			|___ requirements.txt")
				print("		|")

			os.mkdir(project_name_folder)





	#__init__.py for app package
	fp=open(parent_folder+"/"+files[0],"w")
	fp.writelines(data.init_main)
	fp.close()
	print("		|")
	print("		%s"	% files[0])
	print("		|")

	#main_app.py file
	fp=open(parent_folder+"/"+files[6],"w")
	fp.writelines(data.main_application_data)
	fp.close()
	print("		%s" % files[6])
	print("		|")

	#README.md file
	fp=open(parent_folder+"/"+files[7],"w")
	fp.writelines(data.readme_data)
	fp.close()
	print("		%s" % files[7])
	print("		|")

	#run_app.sh file
	fp=open(parent_folder+"/"+files[8],"w")
	fp.writelines(data.shell_data)
	fp.close()
	print("		%s" % files[8])
	print("")

	# generate requirements.txt in doc folder file to use with pip
	fp=open(parent_folder+"/doc/"+files[9],"w")
	fp.writelines(data.req_data)
	fp.close()


# Main function to be executed at run time
#-------------------------------------------------------------------
def main():
	parser = argparse.ArgumentParser(description="Tool to generate flask-odoo-mvc \
	file and folder structure.")
	parser.add_argument("-p","--project", help="path containing your project name",default="test_flask_project")
	args = parser.parse_args()
	project_name=args.project
	if project_name != "":
		project_name=project_name.split()

	for projo in project_name:
		try:
			print("\nCreating project %s....\n"% projo)
			create_project_files(projo)

		except FileExistsError:
			print("  Error: file already exists delete or rename your project.")
			exit()
		else:
			print("Files and folders created successfully!!!\n")




if __name__=='__main__':
	main()
