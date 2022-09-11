# Ecrire un programme qui demande 3 points d'un plans et indique si ils sont allignés.

coa = list(input('co a? \n'))
cob = list(input('co b? \n'))
coc = list(input('co c? \n'))
    

ab = [int(cob[0]) - int(coa[0]), int(cob[-1]) - int(coa[-1])]
cb = [int(cob[0]) - int(coc[0]), int(cob[-1]) - int(coc[-1])]

if ab[0] * cb[-1] - ab[-1] * cb[0] == 0:
	print('les points sont allignés')
else:
	print('les points ne sont pas allignés')

