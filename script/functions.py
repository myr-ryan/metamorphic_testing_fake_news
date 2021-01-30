import re


def filter_emoji(desstr,restr=''):     
    try:  
        res= re.compile(u'[\U00010000-\U0010ffff]')  
    except re.error:  
        res = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')  
    return res.sub(restr, desstr)

def print_label(output):

	labels = []
	for i in range(int(len(output.splitlines()) / 2)):
		labels.append(output.splitlines()[2 * i])

	labels = sorted(labels)

	return labels