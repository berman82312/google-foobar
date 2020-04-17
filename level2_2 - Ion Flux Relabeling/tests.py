import unittest
import solution

class SolutionTest(unittest.TestCase):
  def test1(self):
    self.assertEqual([-1, 7, 6, 3], solution.solution(3, [7, 3, 5, 1]))

  def test2(self):
    self.assertEqual([21, 15, 29], solution.solution(5, [19, 14, 28]))

  def test3(self):
    self.assertEqual([-1, 1019, 15, 268, 603], solution.solution(10, [1023, 987, 14, 266, 599]))

  def test4(self):
    self.assertEqual(
      [-1, 971803, 3391, 22, 803, 343, 12346, 8342663, 18192926, 716253421, 2050, 8194, 16383, 32767],
      solution.solution(30, [1073741823, 971802, 3390, 21, 801, 342, 12345, 8342661, 18192922, 716253420, 2048, 8192, 8191, 16383])
    )

  def test5(self):
    inputs = [835764762, 112110031, 394168102, 15347844, 835677130, 407156346, 894482369, 486655990, 829636825, 1019575011, 940310916, 811074561, 374722533, 890439920, 889000044, 639668559, 153824338, 783059699, 1046820947, 885093408, 25238534, 936748358, 905581083, 567589229, 297194397, 960225129, 324434488, 1011415684, 79786988, 496755922, 721812492, 710817462, 1026564172, 1011261008, 389229416, 207202791, 727511905, 241260430, 537236626, 134691531, 742816355, 542171552, 382145201, 191573765, 616064933, 69114283, 981819577, 1054468787, 499877170, 787800254, 750219828, 546754201, 266275755, 303786269, 916058525, 360105580, 238731693, 4262971, 864598400, 300351506, 812735524, 961295431, 205488669, 801312713, 241616090, 697363786, 170625731, 59166820, 961684411, 73560282, 501840723, 308368967, 756046428, 1010317971, 581465173, 142035906, 1049197880, 988445559, 14528645, 116244037, 715414189, 59227972, 236969923, 21727983, 480601794, 938943205, 961207654, 340611434, 387847557, 709997141, 936364064, 299630183, 499510191, 174293595, 976034732, 460300137, 433773329, 1047779691, 570597358, 258228110, 150152437, 573738377, 915562980, 870706644, 386727489, 840469703, 697042395, 650802855, 182258203, 924662591, 55269608, 824467079, 761086360, 473902957, 496253173, 531491698, 421031670, 486989232, 953429217, 513232564, 340258452, 41531577, 363841297, 144759783, 488238560, 680000771, 578797573, 498369769, 1000131298, 1004761900, 652280868, 364757044, 961750250, 1026590962, 566988212, 777507219, 428142323, 169721445, 481549443, 460140722, 1011911583, 794447693, 273296459, 481472311, 566709071, 32725922, 873473070, 68717715, 952784097, 773802350, 864684932, 863882830, 1067208936, 24654780, 13607759, 597691782, 734678292, 194925789, 972396526, 581889773, 185141814, 165549850, 480875159, 257049833, 144497348, 37847540, 232709149, 488782182, 79752694, 120891548, 383098599, 866487151, 551053397, 526540587, 49832535, 348153689, 177677373, 315839731, 241990993, 94703412, 918636028, 883794720, 738413217, 126955810, 808872823, 545093461, 375668028, 588736824, 512051174, 152991960, 590148296, 189008045, 455040586, 2982061, 878828011, 506382545, 418227751, 443926279, 219653773, 374809680, 274804397, 508422602, 658464006, 108835771, 1038364994, 386543220, 429758959, 572796354, 180631193, 90062565, 831331537, 859123639, 797223867, 116176985, 726858612, 633115875, 938290331, 676394555, 391106396, 163324285, 839629614, 429741600, 129224593, 875961320, 766521016, 892526411, 75217526, 269207872, 482566318, 109784014, 701216646, 493409795, 755353763, 231098610, 406394553, 461601436, 113829390, 917596403, 93434936, 126992983, 883714887, 209252195, 490031210, 346776363, 495974765, 472162557, 50964990, 108080899, 886292675, 338666638, 736788684, 961129370, 55974386, 1025390650, 263930505, 260921848, 753449715, 308094869, 683253426, 998933552, 507963392, 1056874114, 69413956, 420169051, 321295957, 27279079, 817525817, 151884702, 861116967, 997547203, 236512235, 993496313, 221951993, 280055917, 944205881, 225595410, 922852467, 54665580, 317354074, 776667815, 910700303, 274395272, 526826521, 18801789, 8841936, 43520952, 13859030, 261119949, 406198486, 263146175, 285697257, 42205399, 375420851, 823536465, 1048526790, 230654406, 1530580, 152104014, 104452060, 477318487, 705435664, 11774630, 704793097, 500032609, 242475906, 1036551345, 449864978, 409275732, 139414560, 487664862, 1005019601, 1010859218, 599326031, 900433938, 37304788, 918934073, 105677847, 791972113, 142091004, 536625403, 604002292, 163152117, 5707377, 294439748, 437380655, 717721484, 364807877, 1006068165, 429692753, 5619135, 112828433, 320769594, 1058128895, 721319539, 372239501, 829604810, 803907316, 511690381, 782179704, 623683771, 943712126, 460502709, 275772779, 504606870, 236568915, 522175383, 918926314, 1043959704, 345530558, 59506086, 506689946, 517967715, 588183258, 117563033, 603023766, 413374147, 255405862, 877284069, 541097499, 221155342, 822478139, 987762325, 502356107, 291541628, 61099272, 129530997, 96954539, 465753573, 810536263, 23881503, 1061351214, 870392015, 36209842, 756097410, 658727010, 597855675, 592816430, 180884694, 272923511, 201570655, 473457273, 1046580836, 999930736, 214374231, 442722261, 402469247, 484386685, 560361870, 319845678, 130870320, 754689929, 946678343, 959054330, 693019421, 18240643, 627935071, 190054466, 888465816, 95742567, 569734713, 228528044, 106192597, 219241507, 642660705, 135035662, 339843791, 806889167, 817572340, 149552531, 338790267, 55056656, 35818597, 361922953, 79004318, 821937229, 123721803, 55730139, 328497960, 229665020, 213735057, 817399124, 391885813, 676384955, 1040598295, 791943027, 629674162, 90657575, 887006341, 949161520, 254808979, 911044052, 674327520, 535154477, 888625454, 939534418, 292931637, 1050371816, 101413528, 522123370, 197305504, 882297826, 604104571, 194931247, 1016856079, 787089726, 240213853, 1003029412, 277103295, 955622102, 793778757, 305762816, 964235565, 419588057, 152965287, 856361026, 37485120, 161013919, 450340491, 190414975, 776594807, 974263755, 105734777, 960304505, 222645161, 607286630, 109397523, 610122623, 632834658, 863053479, 668714866, 202996622, 163795661, 126630149, 562238222, 184242111, 595107417, 300267547, 620412350, 316684685, 374583576, 190354719, 574094778, 319078185, 466854169, 585975899, 1023624798, 977147645, 501361407, 533789174, 799371919, 501038430, 1009107171, 585814213, 1060748485, 729294496, 246539473, 841224003, 777029264, 561233158, 620537867, 966758200, 212979781, 843444519, 736495374, 1068765602, 619772969, 752877594, 387116674, 342250838, 231081608, 924140472, 211004071, 58588139, 862326741, 225653898, 134991452, 34782842, 845526133, 652630166, 647644395, 375976435, 779603463, 483753547, 194588260, 51703565, 169866057, 580683641, 955342155, 85397921, 430889205, 620782390, 122998482, 901965166, 373288569, 853383342, 27755904, 70959834, 569643076, 384554443, 599586099, 72836907, 878878311, 338447672, 407487835, 869614323, 169251947, 896567220, 831611491, 262490377, 1042327632, 1052195182, 133518939, 948614355, 581530113, 333708280, 844048753, 326033543, 823136739, 554288227, 715774989, 723188491, 303030873, 150178951, 493953519, 99153234, 359408945, 403555463, 304742735, 955854893, 909413544, 1015288242, 476208651, 667367233, 146206432, 702410113, 691931901, 80189138, 981941197, 619125186, 736271300, 862207880, 332044574, 280441527, 335905323, 880660354, 458950591, 475153120, 903093485, 506147078, 1020310490, 272307169, 1027513842, 227187674, 1070342855, 1037934078, 545050742, 884317319, 602990583, 662138193, 969056660, 482615593, 385174187, 403155050, 810309495, 298735349, 930820825, 824730777, 397164046, 228227000, 504415916, 977578841, 131747462, 420469693, 270879258, 721753584, 331212657, 802616012, 767768541, 217855347, 1061263581, 941747748, 92164846, 498160914, 767154441, 450522737, 773952932, 45715980, 236156517, 626806548, 832179776, 308389005, 771215997, 199849510, 541000829, 673287866, 702796084, 273363263, 705401299, 730919033, 915964483, 961023574, 314532261, 837815985, 875537684, 714009073, 243268864, 479649080, 628786149, 220206865, 984447123, 68599940, 702056849, 811425282, 969933921, 355128871, 1032680497, 590684065, 317499888, 40627069, 143045290, 770772858, 280724328, 205734507, 796790276, 935917417, 712398348, 1000198299, 938157678, 634996689, 779639609, 891630893, 632933698, 546012556, 1032011741, 653430115, 903369475, 480656226, 92256391, 816436124, 531879601, 352063758, 996815980, 705234103, 252155475, 668660897, 382101330, 798257715, 811132423, 1052489440, 742918117, 734766074, 577817086, 864346449, 1056305459, 935221567, 186051267, 90767760, 196506963, 932850353, 756930877, 747460716, 684637709, 984277507, 677921119, 203582280, 402655741, 356856830, 981770712, 1005552985, 117692433, 651394655, 508534988, 980511260, 634639126, 675527412, 385659760, 715208425, 859080305, 621473802, 565281147, 1045351048, 363088974, 414763184, 568111599, 818263565, 826353415, 1014899643, 521334241, 104256650, 604980348, 923594623, 706237828, 427985142, 965219857, 893212515, 907983962, 972690102, 1055570000, 477062873, 803471217, 477583166, 295689093, 1027985795, 715356300, 200266784, 117249504, 1016108127, 490328055, 177883762, 317743019, 770307192, 507046344, 108735553, 11173877, 659532671, 1047950746, 310795035, 152240114, 503503089, 948182841, 610204526, 506701457, 429997672, 270848130, 800457118, 740143811, 956722305, 263213936, 166253094, 177866123, 350793803, 1058788569, 329925013, 830059193, 207784171, 221080508, 631149033, 892487009, 358720363, 73784417, 14937941, 93981968, 236298043, 23958996, 813634032, 3120959, 244143969, 478250723, 363451861, 374991375, 805733134, 1020944426, 996717674, 1038993615, 229565666, 562083993, 586694566, 406242909, 839204235, 462573878, 307927693, 18931157, 907160904, 61560574, 417996110, 728592212, 650768677, 998519509, 73790305, 128461144, 472686317, 281547693, 824182487, 876852950, 528322824, 902006914, 572986099, 125724152, 991693203, 212652275, 518167762, 876150991, 164099896, 92245963, 1037212582, 981957681, 1041751811, 958611883, 852815000, 630214699, 86476238, 368266377, 463564924, 421615903, 813251131, 939829009, 538943848, 216910431, 804419184, 747031849, 297463905, 145377915, 592086524, 1003481409, 732610877, 335073927, 894716671, 1024254182, 1040449158, 644769491, 1006405929, 927797215, 857897822, 474642852, 395831223, 15826996, 976256705, 382534880, 425301681, 84253941, 733093763, 859678181, 385715139, 873473125, 865877965, 813380467, 65676824, 343906674, 188893332, 120969542, 133702838, 865991819, 488846809, 422088276, 320381241, 50213328, 352812653, 561167074, 66749286, 107334032, 1004948586, 675683540, 433745086, 390322797, 1042477894, 567802854, 695302461, 974433550, 793007661, 496213445, 684666159, 906745048, 234805389, 813075660, 897775152, 534368906, 158261714, 365052973, 439522275, 696260682, 980238451, 600904312, 468217760, 897351497, 814079237, 628993283, 460873357, 925930994, 793962179, 573241479, 344737659, 51223205, 227537816, 987531862, 565303288, 263320912, 517796359, 602840489, 768760898, 848217283, 225358788, 897076462, 104368985, 258097609, 27790642, 317089311, 127745507, 181148769, 895064112, 410744036, 691992129, 276679246, 128579415, 824348970, 438842928, 351289431, 933766792, 811574229, 1034140235, 367870976, 56844255, 970720713, 528709254, 709067966, 1046569909, 294313675, 165911432, 233588863, 306551142, 532539957, 931625357, 773248437, 577683332, 881285480, 656089552, 681003672, 541211286, 1016767176, 694961920, 175839049, 684160254, 397285719, 148552608, 1038895758, 74062442, 784908308, 568013342, 525775379, 792000152, 128111427, 991780011, 796135680, 548116040, 408224368, 206413667, 804903575, 684590424, 787251013, 844443667, 505864714, 1007800837, 886195970, 727884183, 422288229, 834552286, 517778020, 62067402, 659765275, 100596029, 21517404, 517806065, 106380149, 522392065, 888873465, 515100557, 777825529, 177643451, 766558572, 7760177, 757896622]
    outputs = [835764764, 112110032, 394168103, 15347845, 835677132, 407156348, 894482385, 486655991, 829636826, 1019575013, 940310918, 811074569, 374722534, 890439921, 889000048, 639668561, 153824339, 783059700, 1046820949, 885093410, 25238535, 936748359, 905581085, 567589231, 297194399, 960225130, 324434489, 1011415685, 79786989, 496755923, 721812493, 710817464, 1026564173, 1011261009, 389229424, 207202792, 727511906, 241260432, 537236630, 134691532, 742816357, 542171553, 382145202, 191573769, 616064937, 69114291, 981819579, 1054468789, 499877171, 787800255, 750219829, 546754202, 266275756, 303786271, 916058526, 360105582, 238731697, 4263035, 864598401, 300351508, 812735540, 961295435, 205488671, 801312714, 241616098, 697363794, 170625732, 59166821, 961684419, 73560284, 501840725, 308368968, 756046436, 1010318003, 581465205, 142035922, 1049197888, 988445567, 14528661, 116244038, 715414193, 59227976, 236969924, 21727985, 480601810, 938943213, 961207655, 340611435, 387847558, 709997143, 936364080, 299630184, 499510192, 174293596, 976034734, 460300138, 433773361, 1047779692, 570597360, 258228111, 150152438, 573738379, 915562981, 870706645, 386727505, 840469704, 697042396, 650802856, 182258204, 924662592, 55269609, 824467083, 761086361, 473902958, 496253429, 531491702, 421031672, 486989233, 953429218, 513232568, 340258453, 41531578, 363841329, 144759785, 488238562, 680000773, 578797575, 498369777, 1000131302, 1004761901, 652280869, 364757108, 961750252, 1026590963, 566988214, 777507220, 428142324, 169721447, 481549444, 460140723, 1011911585, 794447694, 273296461, 481472312, 566709072, 32725924, 873473071, 68717717, 952784098, 773802351, 864684948, 863882831, 1067208938, 24654788, 13607761, 597691798, 734678294, 194925791, 972396527, 581889774, 185141815, 165549858, 480875163, 257049834, 144497350, 37847541, 232709150, 488782186, 79752695, 120891556, 383098601, 866487152, 551053398, 526540589, 49832536, 348153691, 177677381, 315839732, 241991025, 94703413, 918636029, 883794721, 738413219, 126955811, 808872827, 545093463, 375668030, 588736826, 512051175, 152991961, 590148297, 189008046, 455040590, 2982062, 878828015, 506382546, 418227752, 443926280, 219653777, 374809681, 274804399, 508422606, 658464007, 108835772, 1038365010, 386543221, 429758960, 572796355, 180631195, 90062566, 831331538, 859123640, 797223868, 116176986, 726858616, 633115876, 938290333, 676394556, 391106397, 163324293, 839629615, 429741601, 129224595, 875961328, 766521017, 892526413, 75217530, 269207873, 482566322, 109784016, 701216647, 493409811, 755353764, 231098611, 406394555, 461601440, 113829391, 917596404, 93434937, 126992984, 883714888, 209252199, 490031218, 346776365, 495974766, 472162558, 50964991, 108080900, 886292691, 338666642, 736788685, 961129372, 55974387, 1025390658, 263930513, 260921850, 753449971, 308094870, 683253490, 998933553, 507963394, 1056874115, 69413957, 420169052, 321295959, 27279083, 817525818, 151884703, 861116968, 997547205, 236512236, 993496321, 221951995, 280055925, 944205883, 225595411, 922852468, 54665581, 317354075, 776667819, 910700305, 274395276, 526826523, 18801797, 8841938, 43520954, 13859031, 261119950, 406198488, 263146176, 285697258, 42205400, 375420915, 823536466, 1048526792, 230654407, 1530581, 152104016, 104452062, 477318488, 705435666, 11774631, 704793099, 500032611, 242475908, 1036551346, 449864979, 409275733, 139414564, 487664866, 1005019602, 1010859219, 599326032, 900433939, 37304820, 918934074, 105677848, 791972114, 142091006, 536625405, 604002293, 163152118, 5707378, 294439764, 437380657, 717721486, 364807879, 1006068173, 429692754, 5619137, 112828435, 320769595, 1058128899, 721319543, 372239502, 829604812, 803907320, 511690382, 782179712, 623683772, 943712127, 460502711, 275772781, 504606871, 236568916, 522175391, 918926316, 1043959706, 345530566, 59506087, 506689947, 517967716, 588183259, 117563034, 603023768, 413374163, 255405863, 877284070, 541097501, 221155344, 822478143, 987762327, 502356108, 291541630, 61099273, 129530998, 96954541, 465753574, 810536264, 23881507, 1061351215, 870392017, 36209846, 756097412, 658727011, 597855683, 592816432, 180884726, 272923513, 201570659, 473457277, 1046580840, 999930864, 214374233, 442722263, 402469248, 484386686, 560361874, 319845679, 130870321, 754689933, 946678345, 959054331, 693019422, 18240645, 627935072, 190054467, 888465824, 95742568, 569734721, 228528045, 106192598, 219241508, 642660706, 135035664, 339843795, 806889168, 817572341, 149552532, 338790268, 55056658, 35818598, 361922957, 79004320, 821937231, 123721807, 55730140, 328497961, 229665021, 213735058, 817399125, 391885814, 676384957, 1040598296, 791943155, 629674164, 90657577, 887006345, 949161521, 254808980, 911044054, 674327521, 535154478, 888625455, 939534419, 292931701, 1050371820, 101413532, 522123372, 197305506, 882297827, 604104572, 194931248, 1016856111, 787089730, 240213855, 1003029413, 277103296, 955622103, 793778759, 305762817, 964235569, 419588058, 152965289, 856361028, 37485121, 161013920, 450340495, 190414977, 776594809, 974263763, 105734781, 960304506, 222645162, 607286634, 109397524, 610122624, 632834659, 863053480, 668714867, 202996624, 163795662, 126630165, 562238230, 184242127, 595107425, 300267555, 620412351, 316684687, 374583578, 190354723, 574094782, 319078186, 466854170, 585975907, 1023624802, 977147649, 501361409, 533789176, 799371920, 501038446, 1009107187, 585814214, 1060748493, 729294497, 246539474, 841224004, 777029266, 561233160, 620537875, 966758202, 212979797, 843444521, 736495376, 1068765604, 619772977, 752877596, 387116690, 342250839, 231081612, 924140473, 211004073, 58588140, 862326743, 225653906, 134991460, 34782844, 845526135, 652630170, 647644397, 375976436, 779603471, 483753549, 194588261, 51703566, 169866059, 580683643, 955342159, 85397923, 430889206, 620782391, 122998514, 901965167, 373288570, 853383343, 27755908, 70959835, 569643077, 384554444, 599586100, 72836909, 878878312, 338447673, 407487836, 869614324, 169251948, 896567222, 831611492, 262490378, 1042327634, 1052195183, 133518943, 948614387, 581530115, 333708281, 844048754, 326033545, 823136740, 554288228, 715774993, 723188495, 303030874, 150178955, 493953520, 99153266, 359408946, 403555465, 304742743, 955854897, 909413545, 1015288243, 476208659, 667367235, 146206448, 702410114, 691931903, 80189139, 981941198, 619125202, 736271302, 862207888, 332044578, 280441531, 335905327, 880660358, 458950592, 475153122, 903093486, 506147079, 1020310491, 272307170, 1027513844, 227187676, 1070342856, 1037934079, 545050870, 884317320, 602990584, 662138194, 969056692, 482615597, 385174191, 403155051, 810309496, 298735351, 930820829, 824730781, 397164047, 228227008, 504415918, 977578842, 131747464, 420469694, 270879259, 721753585, 331212659, 802616013, 767768542, 217855475, 1061263583, 941747750, 92164847, 498160915, 767154443, 450522738, 773952934, 45715981, 236156521, 626806550, 832179778, 308389013, 771215998, 199849511, 541000830, 673287868, 702796086, 273363265, 705401300, 730919035, 915964484, 961023576, 314532263, 837815986, 875537686, 714009074, 243268865, 479649081, 628786151, 220206869, 984447124, 68599942, 702056850, 811425283, 969933923, 355128873, 1032680498, 590684081, 317499889, 40627073, 143045291, 770772860, 280724329, 205734508, 796790280, 935917419, 712398349, 1000198303, 938157679, 634996721, 779639617, 891630897, 632933700, 546012557, 1032011742, 653430116, 903369491, 480656228, 92256392, 816436125, 531879602, 352063759, 996815982, 705234104, 252155507, 668660898, 382101362, 798257779, 811132424, 1052489442, 742918119, 734766075, 577817094, 864346450, 1056305461, 935221583, 186051269, 90767761, 196506964, 932850354, 756930879, 747460717, 684637711, 984277523, 677921121, 203582284, 402655743, 356856838, 981770714, 1005552989, 117692435, 651394671, 508534992, 980511261, 634639128, 675527413, 385659761, 715208433, 859080306, 621473804, 565281149, 1045351056, 363088975, 414763185, 568111600, 818263566, 826353417, 1014899647, 521334242, 104256651, 604980349, 923594624, 706237829, 427985143, 965219859, 893212517, 907983963, 972690104, 1055570032, 477062874, 803471219, 477583167, 295689094, 1027985797, 715356301, 200266800, 117249520, 1016108131, 490328056, 177883763, 317743023, 770307200, 507046352, 108735554, 11173878, 659532672, 1047950748, 310795036, 152240115, 503503090, 948182843, 610204527, 506701458, 429997673, 270848131, 800457120, 740143813, 956722306, 263213937, 166253095, 177866124, 350793804, 1058788573, 329925045, 830059201, 207784172, 221080512, 631149035, 892487010, 358720365, 73784418, 14937945, 93981972, 236298045, 23958998, 813634033, 3120961, 244143985, 478250724, 363451863, 374991376, 805733135, 1020944434, 996717675, 1038993647, 229565667, 562083994, 586694567, 406242910, 839204243, 462573880, 307927694, 18931189, 907160906, 61560578, 417996112, 728592213, 650768681, 998519510, 73790306, 128461148, 472686318, 281547701, 824182519, 876852952, 528322832, 902006915, 572986100, 125724153, 991693204, 212652276, 518167764, 876150992, 164099904, 92245964, 1037212590, 981957682, 1041751813, 958611891, 852815001, 630214701, 86476242, 368266385, 463564932, 421615904, 813251139, 939829011, 538943850, 216910432, 804419312, 747031850, 297463906, 145377917, 592086525, 1003481413, 732610878, 335073928, 894716675, 1024254184, 1040449159, 644769492, 1006405930, 927797231, 857897823, 474642853, 395831225, 15826997, 976256721, 382534881, 425301682, 84253942, 733093764, 859678182, 385715141, 873473126, 865877966, 813380595, 65676828, 343906802, 188893333, 120969544, 133702839, 865991820, 488846817, 422088277, 320381242, 50213329, 352812654, 561167076, 66749288, 107334033, 1004948590, 675683541, 433745087, 390322798, 1042477895, 567802855, 695302465, 974433554, 793007665, 496213446, 684666160, 906745049, 234805390, 813075661, 897775153, 534368910, 158261746, 365052981, 439522277, 696260683, 980238452, 600904313, 468217762, 897351499, 814079239, 628993284, 460873358, 925930995, 793962183, 573241483, 344737660, 51223207, 227537818, 987531864, 565303289, 263320944, 517796360, 602840493, 768760914, 848217299, 225358790, 897076463, 104368987, 258097610, 27790644, 317089313, 127745509, 181148770, 895064113, 410744038, 691992131, 276679248, 128579423, 824348972, 438842930, 351289463, 933766793, 811574231, 1034140237, 367870978, 56844256, 970720721, 528709255, 709067968, 1046569913, 294313676, 165911433, 233588867, 306551143, 532539958, 931625358, 773248441, 577683334, 881285481, 656089553, 681003674, 541211287, 1016767177, 694961922, 175839057, 684160258, 397285720, 148552609, 1038895759, 74062443, 784908309, 568013346, 525775381, 792000154, 128111443, 991780013, 796135682, 548116042, 408224372, 206413668, 804903576, 684590428, 787251021, 844443668, 505864715, 1007800853, 886195971, 727884187, 422288231, 834552287, 517778022, 62067403, 659765283, 100596030, 21517406, 517806066, 106380150, 522392067, 888873466, 515100558, 777825530, 177643452, 766558573, 7760178, 757896623]
    self.assertEqual(outputs, solution.solution(30, inputs))

if __name__ == '__main__':
  unittest.main()