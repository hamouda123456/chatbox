import openai
import sys
from pymongo import MongoClient

url_mongo = "mongodb+srv://ahmed:ahmed@cluster0.iaanx.mongodb.net/Twilio?retryWrites=true&w=majority"
client = MongoClient(url_mongo)
db = client['Twilio_DB']
sys.stdout = open('url.txt', 'w', encoding='utf-8')
openai.api_key = ""
url1 = "https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/RE671ba637f68fe8467f7c9cfa9cfce481"
transcript1 = "customer:[0:00:00]Oui allo?  agent:[0:00:01]Madame Romanance?  customer:[0:00:02]Oui?  agent:[0:00:03]C'est de la part de Yalow, l'opérateur téléphonique mobile.  customer:[0:00:07]Pardon?  agent:[0:00:08]C'est Yalow, l'opérateur mobile Yalow.  customer:[0:00:11]Oui?  agent:[0:00:12]On t'ait permis de vous contacter puisque vous avez consulté le site Sapiens qui va vendre,  agent:[0:00:16]donc on revient vers vous avec les offres de Yalow.  agent:[0:00:19]Par rapport à votre abonnement actuellement, madame, celui qui se termine par 62,65, vous êtes avec Swisscal, c'est ça?  customer:[0:00:25]Oui.  customer:[0:00:00.008001]Oui  agent:[0:00:00.024997] Vous avez profité d'une offre avec Yalow ou pas encore, madame?  customer:[0:00:31]Non, mais je vais changer tout tout prochainement, là.  agent:[0:00:34]C'est-à-dire?  customer:[0:00:36]Je vais changer d'abonnement, mais ce ne sera pas chez vous, donc ce sera peut-être plus tard chez vous.  customer:[0:00:40]Là, je vais changer d'abonnement sur tous.  agent:[0:00:00.016409]Vous avez passé avec qui  agent:[0:00:00.028269] Excusez-moi, je n'ai pas entendu.  customer:[0:00:48]Mais je ne vous ai pas dit avec qui vous avez passé, parce que… qu'est-ce que vous me proposez?  customer:[0:00:52]Allez-y, dites-moi ce que vous me proposez.  agent:[0:00:00.020339]D'accord. Dites-moi, qu'est-ce que vous, vous cherchez  agent:[0:00:00.032297] Est-ce que vous cherchez uniquement en Suisse  customer:[0:00:00.032297]  customer:[0:00:00.013081]Moi, je ne cherche rien  customer:[0:00:00.036994] Moi, je ne cherche rien du tout  customer:[0:00:00.068994] Je n'ai besoin de rien  agent:[0:00:00.068994]  agent:[0:01:03]Si vous trouvez une formule intéressante, ça ne pourra pas vous intéresser?  customer:[0:01:08]Parlez-moi de votre formule.  agent:[0:00:00.008890]Oui, madame  agent:[0:00:00.014889] D'accord  agent:[0:00:00.034909] Vous avez besoin d'une offre, c'est-à-dire en Suisse seulement ou bien vers l'Europe aussi?  customer:[0:01:17]Non.  agent:[0:00:00.015997]J'ai voulu… Voilà  agent:[0:00:00.030094] Vous avez besoin uniquement en Suisse?  customer:[0:01:22]Oui.  agent:[0:01:24]Je vous propose dans ce cas-là un abonnement de tout illimité en Suisse, que ce soit les appels, Internet et SMS à 23 francs.  customer:[0:01:31]Mais là, je viens de faire un abonnement à 12 francs.  agent:[0:01:34]À 12 francs avec Internet illimité et tout ça, madame?  customer:[0:01:39]Tout.  agent:[0:00:00.009999]Si vous le dites  agent:[0:00:00.020087] Vérifiez le contrat, tout simplement  agent:[0:00:00.027003] Voilà  agent:[0:00:00.037998] Il n'y a pas de problème  customer:[0:00:00.046004] Merci  customer:[0:00:00.047002]  customer:[0:00:00.008040]Merci à vous  customer:[0:00:00.008040]"
url2="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/REc3c4ab93d417354cc4eda00253acb6d0"
transcript2="agent:[0:00:00]Allo?  agent:[0:00:02]Oui, bonjour madame, je suis Céline de l'opérateur téléphonique Allo, et on se permet de vous contacter parce que nous mettons à votre disposition des rabais allant jusqu'à 70%, c'est donc pour vous en faire profiter.  customer:[0:00:15]Attendez, attendez, je vais parler de France, parce que je ne comprends pas bien le français.  customer:[0:00:25]Ok, et vous ne parlez pas l'espagnol?  agent:[0:00:28]Non, désolée.  customer:[0:00:30]Attendez un moment, s'il vous plaît.  agent:[0:00:33]Débora!  agent:[0:00:48]Oui, allo?  agent:[0:00:49]Oui, bonjour madame, je suis Céline de l'opérateur téléphonique Allo.  customer:[0:00:54]Oui?  agent:[0:00:55]Et on se permet de vous contacter parce que nous mettons à votre disposition des rabais allant jusqu'à 70%, c'est pour vous en faire profiter.  customer:[0:01:05]Pourquoi, pardon?  agent:[0:01:08]Parce que nous mettons à votre disposition des rabais, très intéressant, c'est donc pour vous en faire profiter.  customer:[0:01:13]Oui, mais sur quoi?  agent:[0:01:15]Sur mes abonnements téléphoniques, pour le Nacelle, pour Internet maison, également pour les Box TV.  customer:[0:01:23]Oui, non, on n'est pas intéressé, on a déjà des abonnements de téléphone, ça joue comme ça, on est bien.  agent:[0:01:30]D'accord madame, peut-être à la prochaine, au revoir.  customer:[0:01:33]Merci."
url3="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/REfdd417aeedd72764ee852a61281f651a"
transcript3="agent:[0:00:01]Ça va, vous?  customer:[0:00:03]Allô, bonjour.  agent:[0:00:05]Oui, bonjour madame.  agent:[0:00:06]Je suis Cyrus de l'opérateur téléphonique Yano.  agent:[0:00:09]Et on se permet de vous contacter parce que nous mettons à votre disposition des rabais allant jusqu'à 70%  agent:[0:00:15]et donc pour vous en faire profiter.  agent:[0:00:18]Euh, des rabais sur quoi?  agent:[0:00:21]Sur les nouveaux abonnements téléphoniques, donc ça concerne le Nathen, Internet maison et également les vox TV.  customer:[0:00:27]Euh, non merci, j'ai pas besoin.  agent:[0:00:31]Vous pouvez avoir une idée sur Nathen, ça peut vous intéresser par la suite à vous de décider, madame.  customer:[0:00:38]D'accord.  agent:[0:00:40]Donc, actuellement pour cette ligne, vous êtes avec quel opérateur?  customer:[0:00:46]La Camobile, mais je peux pas faire d'abonnement parce que je sais pas, ils m'ont dit que j'ai un facture ou je sais pas quoi.  agent:[0:00:53]Parce que quoi, pardon?  customer:[0:00:54]Euh, je peux pas faire d'abonnement parce que j'étais en retard pour payer une facture, donc.  agent:[0:01:02]D'accord, donc vous ne pouvez pas faire d'abonnement chez La Camobile uniquement ou bien chez Yalo?  customer:[0:01:09]Non.  agent:[0:01:10]Vous avez essayé?  customer:[0:01:11]Oui, j'avais essayé chez Yalo, mais je peux pas.  agent:[0:01:15]D'accord, vous voulez qu'on fasse un essai?  customer:[0:01:18]Si jamais, j'ai déjà essayé deux fois, mais ça n'a pas marché et tout.  agent:[0:01:24]D'accord, même avec un autre numéro?  customer:[0:01:27]Oui.  agent:[0:01:29]D'accord, donc peut-être à la prochaine dans ce cas.  customer:[0:01:33]Oui, au revoir.  agent:[0:01:34]Au revoir."
url4="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/RE98a9666695552e6cf53b3443173f882e"
transcript4="agent:[0:00:00.011695] Bonjour  customer:[0:00:02.800000]Oui, allô?  agent:[0:00:00.005001]Allô  agent:[0:00:00.011001] Oui, bonjour madame.  customer:[0:00:05.600000]Oui?  agent:[0:00:06.300000]Je me présente, je suis l'opérateur Céline Gallo.  agent:[0:00:09.200000]Et je vous permets de vous contacter parce qu'on a lancé de nouvelles promotions qui devraient jusqu'à 700% à vie pour toujours.  agent:[0:00:16.300000]Donc, vous madame, vous êtes chez quel opérateur s'il vous plaît?  customer:[0:00:19.400000]Euh, moi je suis chez Cisco, mais je ne comprends pas le message de l'opérateur. Je suis désolée.  agent:[0:00:00.015999]Je n'ai pas compris, vous dites  agent:[0:00:00.021000] Pardon  customer:[0:00:00.021000]  agent:[0:00:29.300000]Je dis que c'est Swisscom.  agent:[0:00:32.100000]D'accord. Vous appuyez juste en Suisse avec Swisscom ou bien vous appuyez aussi vers l'Europe?  customer:[0:00:38.100000]Je n'appelle pas l'Europe, je ne connais personne là-bas.  agent:[0:00:42.300000]D'accord. Et vous payez combien votre abonnement sans indiscrétion?  customer:[0:00:46.500000]Euh, ben, ça, la maison.  agent:[0:00:49.800000]Ah, c'est un paiement en paiement que vous avez?  customer:[0:00:52.700000]Ah?  agent:[0:00:53.700000]C'est le paiement en paiement avec Internet maison et tout?  customer:[0:00:56.700000]Oui, oui.  agent:[0:00:58]Et c'est à combien avec Swisscom madame pour le tout?  customer:[0:01:02]Euh, 200, 200 quelque chose.  agent:[0:01:06.300000]Donc, c'est avec le Napel, la télé, la fibre, c'est ça?  customer:[0:01:09.900000]Oui.  agent:[0:01:12.200000]D'accord. C'est un peu trop cher madame. Moi, je peux vous proposer mieux en qualité et moins cher en prix.  customer:[0:01:21.200000]Euh, je ne sais pas. En fait, il y a des gens vraiment occupés, je n'ai pas les…  agent:[0:01:28.200000]Ah, d'accord. Voilà.  agent:[0:01:30.200000]Des gens occupés, des gens qui ont…  agent:[0:01:32.200000]Je peux éventuellement les demander.  customer:[0:01:34.200000]Oui, vous pouvez m'appeler demain.  customer:[0:01:36.200000]Oui, c'est mieux.  customer:[0:01:37.200000]À cette heure-ci, ça va?  customer:[0:01:39.200000]Oui, ça va pour moi.  agent:[0:01:41.200000]D'accord. Merci madame.  customer:[0:01:42.200000]Au revoir.  customer:[0:01:43.200000]Au revoir."
url5="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/REafb1c3c56bd8840ce3c0b663acf2f4cb"
transcript5="customer:[0:00:00]Allo?  agent:[0:00:01]Oui, bonjour.  customer:[0:00:02]Bonjour.  agent:[0:00:03]Monsieur Gilles Lindeja?  customer:[0:00:05]Oui, pourquoi?  agent:[0:00:06]C'est l'opérateur téléphonique Yalow, je vous ai contacté l'autre jour, monsieur.  customer:[0:00:10]Ah oui, vous êtes de base, c'est ça?  agent:[0:00:13]Voilà, c'est l'opérateur téléphonique Yalow.  customer:[0:00:16]Oui.  agent:[0:00:17]Je vous ai contacté concernant les nouvelles offres de Yalow, monsieur.  customer:[0:00:24]Oui, mais je vais bientôt avoir le changement au mois de juin, c'est bon.  agent:[0:00:28]D'accord, ça c'est avec Yalow, c'est ça?  customer:[0:00:31]Voilà, c'est ça, oui.  agent:[0:00:33]Et pour Internet à la maison, monsieur, vous êtes avec qui?  customer:[0:00:36]Pour le moment, je suis avec UPC.  agent:[0:00:39]Très très bien.  agent:[0:00:40]Avec UPC, votre abonnement, il vous coûte combien mensuellement, s'il vous plaît?  customer:[0:00:44]Oh, j'ai pu tous les détails, mais le changement va flir bientôt, monsieur, avec Yalow.  customer:[0:00:49]C'est bon.  agent:[0:00:50]Oui, non, non, ça c'est pour la partie Nathel, on est bien d'accord.  agent:[0:00:53]Je parle pour la partie Internet à la maison, parce que pour les personnes qui ont des abonnements avec Yalow,  agent:[0:01:00]ils profiteront des offres très intéressantes pour la partie Internet, et surtout que vous, vous êtes avec UPC,  agent:[0:01:06]donc on garde la même technologie.  agent:[0:01:08]Par contre, pour la partie facturation, on peut vous proposer une formule moins chère par rapport à ce que vous avez.  agent:[0:01:13]Parce que c'est bien plus cher que vous, vous êtes au minimum à 58, 60 francs par mois, pour la partie Internet.  customer:[0:01:19]Oui, c'est plus.  customer:[0:01:20]Oui?  customer:[0:01:21]Oui, je sais plus.  agent:[0:01:22]Oui, voilà, c'est ça, l'offre basique, bien sûr, de UPC.  agent:[0:01:25]Puisque c'est UPC de Sunrise, et nous, on est Yalow de Sunrise.  customer:[0:01:29]Oui, oui, oui, mais j'ai mon vendeur qui va faire le nécessaire au mois de juin, là, c'est bon.  customer:[0:01:36]Le basculement va se faire.  agent:[0:00:00.015989]Vous parlez de quoi, monsieur  agent:[0:00:00.035103] Vous parlez de l'Internet à la maison ou bien du Nathel  customer:[0:00:00.036108]  customer:[0:01:41]De tout, de tout, du tout, l'Internet, la télé et le téléphone, voilà.  agent:[0:01:47]D'accord, il n'y a pas de problème, merci infiniment.  customer:[0:00:00.046537]OK, merci monsieur, c'est gentil, merci  agent:[0:00:00.046537]"
url6="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/REe7e4534c32f138367e5b4469b89d0492"
Recording6="agent:[0:00:00]Oui, bonjour, madame.  agent:[0:00:02]Je suis Cyrille, de l'opérateur téléphonique Allo,  agent:[0:00:05]et on se permet de vous contacter parce que nous mettons  agent:[0:00:08]à votre disposition des rabais allant jusqu'à un 70 %.  agent:[0:00:11]C'est donc pour vous en faire profiter.  customer:[0:00:15]Ah non, merci.  agent:[0:00:17]Vous pouvez avoir l'idée sur nos offres,  agent:[0:00:19]faire un petit comparatif par rapport à ce que vous avez  agent:[0:00:22]actuellement et à vous de voir par la suite.  customer:[0:00:26]En fait, moi, je ne parle pas bien français,  customer:[0:00:28]je ne comprends pas tout ce que vous dites.  agent:[0:00:31]D'accord, on va essayer de faire avec.  agent:[0:00:34]Actuellement, pour cette ligne, vous avez quel opérateur téléphonique?  customer:[0:00:39]C'est Allo.  agent:[0:00:42]Ah d'accord, très bien, vous êtes déjà chez nous.  customer:[0:00:46]Oui, oui, je suis Allo.  agent:[0:00:49]Et pour Internet maison?  customer:[0:00:51]Non, moi, je ne les vends pas.  agent:[0:00:54]D'accord, est-ce que vous voulez parrainer quelqu'un de votre famille  agent:[0:00:59]ou bien de vos proches?  customer:[0:01:01]Maintenant, je suis dans le travail, je ne peux pas parler.  agent:[0:01:06]D'accord, vous voulez que je vous rappelle l'après-midi?  customer:[0:01:10]Non, c'est bon, moi, je ne les vends pas de votre service.  agent:[0:01:18]D'accord, merci, bonne journée.  agent:[0:01:20]Merci, bonne journée.  customer:[0:01:22]Merci."
url7="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/RE4edc414f3c3ca155ab1d1ce86331dd1e"
Recording7="agent:[0:00:00]Oui, bonsoir, monsieur, je suis Cyril de l'opérateur téléphonique Allo.  agent:[0:00:10]Et on se permet de vous contacter parce que nous laissons à votre disposition des rabais allant jusqu'à 70%.  agent:[0:00:18]C'est pour vous en faire profiter.  customer:[0:00:20]Oui, madame, mais moi je ne suis pas encore chez vous.  agent:[0:00:24]Vous avez commencé la portabilité de votre ligne chez Allo?  customer:[0:00:30]Je n'ai pas compris, madame.  agent:[0:00:32]Vous avez déjà fait une démarche pour venir chez Allo?  customer:[0:00:35]Oui, j'ai déjà fait une démarche pour venir chez vous.  customer:[0:00:38]Par contre, il faut que j'attende que mon contrat chez Salt ou Sunrise, je ne me rappelle plus.  agent:[0:00:43]Arrivataire?  customer:[0:00:44]Voilà, c'est ça. Parce que sinon, j'ai déjà tout ce que j'ai, j'ai déjà les cartes SIM, les machins, les trucs.  agent:[0:00:51]Même pour Internet maison?  customer:[0:00:54]Même les?  agent:[0:00:56]Même pour l'abonnement à la maison, pour Internet maison?  customer:[0:01:00]A la maison, je ne veux pas, madame.  agent:[0:01:03]D'accord, et vous avez une box TV actuellement?  customer:[0:01:07]Oui, oui, j'ai une box TV, oui.  agent:[0:01:11]D'accord, donc voilà, on se rappelle plus tard.  customer:[0:01:15]Il n'y a pas de soucis.  agent:[0:01:18]Je vous souhaite une bonne soirée.  customer:[0:01:19]Merci, par ailleurs. Au revoir."
url8="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/RE4453af5700a61cdecb2d52833cd114e9"
Recording8="agent:[0:00:00]Bonsoir Madame, je suis Cyrille de l'opérateur téléphonique Allo, et on se permet de vous  agent:[0:00:09]contacter parce que nous mettons à votre disposition des rabais allant jusqu'à 70%  agent:[0:00:14]et donc pour vous en faire profiter.  customer:[0:00:15.680000]Quand?  agent:[0:00:16.680000]À partir de maintenant, si vous voulez.  customer:[0:00:22.680000]Excusez-moi, vous n'avez pas compris, qu'est-ce que vous avez dit?  agent:[0:00:30.680000]Bonsoir, je disais que c'est l'opérateur téléphonique Allo et nous avons actuellement  agent:[0:00:36.840000]des rabais intéressants, ce qui concerne les abonnements téléphoniques, et donc pour  agent:[0:00:41.520000]vous en faire profiter.  customer:[0:00:42.760000]Ça veut dire des réductions de même abonnement ou c'est de nouveau abonnement?  agent:[0:00:51.760000]Pardon?  customer:[0:00:52.760000]De nouveau abonnement, abonnement ou c'est une réduction de la même abonnement?  agent:[0:01:00.760000]Non, en fait ça concerne les nouveaux abonnements.  customer:[0:01:03.760000]Ah d'accord.  customer:[0:01:04.760000]Non, nous on est bien comme ça, on va continuer tel comme.  customer:[0:01:11.760000]Merci quand même pour votre appel.  agent:[0:01:14.760000]Je vous en prie, je vous souhaite une bonne journée, une bonne soirée, au revoir.  customer:[0:01:18.760000]Parlez-moi."
url9="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/RE47ca6b03a42b28f0fd262e0ded14e896"
Recording9="agent:[0:00:01]Oui, bonjour madame.  customer:[0:00:02]Bonjour.  agent:[0:00:03]Je vous présente, c'est l'opérateur téléphonique Lowe.  agent:[0:00:06]Et j'ai l'intérêt de vous contacter parce qu'on a lancé de nouvelles promotions  agent:[0:00:09]qui peuvent aller jusqu'à 70% à vie pour toujours.  customer:[0:00:12]Écoutez, madame, j'ai déjà fait un abonnement chez vous,  customer:[0:00:00.007090]donc j'attends que je puisse  agent:[0:00:00.008092]  agent:[0:00:00.008092]  customer:[0:00:00.034003] que ça puisse être annulé pour l'autre opérateur  agent:[0:00:00.034003]  agent:[0:00:20]D'accord.  customer:[0:00:21]Je ne sais pas pourquoi vous m'appelez à chaque fois.  agent:[0:00:23]Ah, on vous a beaucoup appelé?  customer:[0:00:26]Oui.  customer:[0:00:27]Trois fois la semaine passée.  agent:[0:00:31]D'accord.  customer:[0:00:32]Donc, je vous dis juste parce que voilà, j'ai l'abonnement et puis l'abonnement.  customer:[0:00:38]J'ai déjà en fait l'offre.  agent:[0:00:40]Oui.  customer:[0:00:41]J'ai déjà le contrat à la maison et tout, donc je serai chez vous l'année prochaine.  agent:[0:00:44]Oui.  customer:[0:00:45]Donc moi, je ne les vois pas.  customer:[0:00:48]C'est juste que vous m'appelez pour rien, quoi.  agent:[0:00:51]Non, peut-être pour Internet à la maison, madame.  customer:[0:00:54]Pardon?  agent:[0:00:55]Pour Internet à la maison.  customer:[0:00:00.006984]Non, mais pour Internet à la maison, je ne peux pas  agent:[0:00:00.006984]  agent:[0:00:00.007988]  agent:[0:00:00.007988]  customer:[0:00:58]Pour l'instant, je ne peux pas annuler parce que sinon, je vais payer beaucoup de frais.  agent:[0:01:03]D'accord.  customer:[0:01:04]Donc, je dois rester encore une année chez eux.  customer:[0:01:05]Donc, voilà.  agent:[0:01:06]D'accord.  agent:[0:01:07]D'accord.  agent:[0:01:08]Je vais tout mentionner, madame, et excusez-moi pour le dérangement encore une fois.  customer:[0:01:10]Non, il n'y a pas de souci.  customer:[0:01:11]Il n'y a pas de souci.  customer:[0:01:12]On dit tout et puis comme ça, c'est réglé.  customer:[0:01:14]Voilà.  agent:[0:01:15]C'est très bien.  agent:[0:01:16]Merci à vous, madame.  agent:[0:01:17]Bonne journée.  customer:[0:01:18]A vous aussi.  customer:[0:01:19]Au revoir.  customer:[0:01:20]Au revoir.  agent:[0:01:21]Merci.  agent:[0:01:22]Merci.  agent:[0:01:23]Merci.  agent:[0:00:00.006999]Merci  agent:[0:00:00.007998]"
url10="https://api.twilio.com/2010-04-01/Accounts/AC4fe689d01a8614e6572adb5df245497b/Recordings/RE6e76461234833fbee8c7d723f7d4f4ca"
Recording10="agent:[0:00:00]Oui, bonjour monsieur, je suis Céline, de l'opérateur téléphonique YALO, et on se permet de vous contacter parce que nous mettons à votre disposition des rabais à moins jusqu'à 70%, et donc pour vous en faire profiter.  customer:[0:00:14]Ah d'accord, merci, en fait, ça va aller comme ça.  agent:[0:00:19]Vous pouvez en partager sur le vôtre, faire un petit comparatif même par rapport à ce que vous payez actuellement et à vos devantages.  customer:[0:00:27]Actuellement, je ne paye rien, je suis en prix payé depuis, je suis très content.  agent:[0:00:32]D'accord, et vous rechargez à l'ordre de combien?  customer:[0:00:36]Je ne charge même pas, en fait. J'ai mis 10 francs, j'ai tenu 5 mois pour l'instant, donc si vous avez un abonnement pour 10 francs 5 mois, moi je suis…  agent:[0:00:48]En fait, non, mais on a un abonnement à 8 francs uniquement par mois.  customer:[0:00:53]Vous voyez, malheureusement, ça ne joue pas.  agent:[0:00:57]D'accord, d'accord, donc peut-être à la prochaine.  customer:[0:01:00]Oui.  agent:[0:01:01]Sinon, vous avez un abonnement pour Internet maison?  customer:[0:01:04]Oui, on a plus de l'info, merci.  agent:[0:01:06]Et vous êtes engagé avec votre opérateur actuel?  customer:[0:01:09]Oui.  agent:[0:01:11]D'accord, mon chien, donc je vous remercie beaucoup pour votre accueil et je vous souhaite une bonne journée.  agent:[0:01:16]Merci, au revoir.  agent:[0:01:17]Au revoir."
urls = [url1,url2,url3,url4,url5,url6, url7, url8, url9, url10]
collections = db["Call_Records_Transcripts"]
collection = db["rejection_argument"]
for url in urls:
    document = collection.find_one({"url": url})
    if document:
        """
        contexte=document.get('transcript')
        prompt_rejection = f" Voici le contexte :\n\n{contexte}\nau début du contexte afficher uniquement et exactement ce que le client a dit  de sa raison de désintérêt :"
        prompt_argument = f" Voici le contexte :\n\n{contexte}\n au début du contexte afficher uniquement et exactement ce que l'agent a dit  juste après la justification de désintérêt du client : "
        collection = db["rejection_argument"]
        response_rejection = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_rejection,
            temperature=0.2,
            max_tokens=100,
        )

        rejection_reason = response_rejection.choices[0].text.strip()
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_argument,
            temperature=0.2,
            max_tokens=100,
        )

        contre_arguments = response.choices[0].text.strip()

        collection.update_one(
            {
                "url": url,
            },
            {
                "$set": {
                    "contre_arguments": contre_arguments,
                    "rejection_reason": rejection_reason,
                }
            },
        )

        keywords_rejection_prompt = f"Voici le contexte :\n\n{rejection_reason}\nAfficher exactement les mots clés de la raison de désintérêt du client d'offre :"
        keywords_argument_prompt = f"Voici le contexte :\n\n{contre_arguments}\nAfficher exactement les mots clés d'agent après la justification de désintérêt du client :"

        keywords_response_rejection = openai.Completion.create(
            engine="text-davinci-002",
            prompt=keywords_rejection_prompt,
            temperature=0.2,
            max_tokens=20,
        )
        keywords_rejection = keywords_response_rejection.choices[0].text.strip().replace("-", "").replace("_", "")

        keywords_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=keywords_argument_prompt,
            temperature=0.2,
            max_tokens=20,
        )
        keywords_contre_arguments = keywords_response.choices[0].text.strip().replace("-", "").replace("_", "")

        collection.update_one(
            {
                "url": url,
                "contre_arguments": contre_arguments,
                "rejection_reason": rejection_reason,
            },
            {
                "$set": {
                    "keywords_rejection": keywords_rejection,
                    "keywords_contre_arguments": keywords_contre_arguments,
                }
            },
        )
             """
        print(f"url : {url}")
        print(f"La raison de rejet est : {document.get('rejection_reason')}")
        print(f"Le contre-argument est : {document.get('contre_arguments')}")
        list_keywords_rejection = document.get("keywords_rejection").split()
        list_keywords_argument = document.get("keywords_contre_arguments").split()
        print(f"Les mots clés de la raison de rejet sont  : {list_keywords_rejection}")
        print(f"Les mots clés du contre-argument sont : {list_keywords_argument}")