#
#   https://github.com/jandiorio/study_group_screen
#
#  Launch the Student VM and Connect with VS Code
# 
#  https://gitlab.com/joelwking/cisco_dc_community_of_interest/-/tree/master/demos/workshop#student-resources
#
#  The key file is at: https://wwt.sharepoint.com/sites/truist-consulting/Shared%20Documents/General/truist.pem
#
#  Configure Git
# $ git config --global user.name "Colleen Katzberg"
# $ git config --global user.email colleen.katzberg@wwt.com
#
#
import yaml

me = []                            # Create an empty list
#                                  # append the dictionary to the list
me.append(dict(first_name='Colleen', 
               last_name='Katzberg', 
               company='WWT', 
               email='colleen.katzberg@wwt.com',
               github_username='@katzberc')
        )

print (me)
                                  # Write the list to a YAML file
with open('outputfile', 'w') as outfile:
    yaml.dump(me, outfile, default_flow_style=False)