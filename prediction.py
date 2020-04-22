import praw
from praw.models import MoreComments
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle, json
from os import environ

config={}

config['c_id'] = environ.get("c_id")
config['c_secret']=environ.get("c_secret")
config['u_a']=environ.get("u_a")
config['usrnm']=environ.get("usrnm")
config['passwd']=environ.get("passwd")

# with open('config_file.json') as config_file:
    # config = json.load(config_file)


def predict(url):
	# print (config)
	reddit = praw.Reddit(client_id = config['c_id'],
	client_secret = config['c_secret'],
	user_agent = config['u_a'],
	username = config['usrnm'],
	password = config['passwd']
	)

	idx_flair= ['AskIndia', 'Business/Finance', 'Food', 'Non-Political', 'Photography', 'Policy/Economy', 'Politics', 'Science/Technology','Sports']


	post = praw.models.Submission(reddit, url=url)
	posts = {
	"title":str(post.title),
	"body":str(post.selftext),
	"flair":str(post.link_flair_text),
	"comms_num":str(post.num_comments),
	}
#  Only top ten comments and their authors are considered. 
	post.comments.replace_more(limit=None)
	comment = str()
	count = 0
	for top_comment in post.comments:
		comment = comment + ' ' + top_comment.body
		count+=1 
		if(count > 10):
			break

	posts["comment"] = str(comment)
	
	X_test=posts["title"] + posts["comment"] + posts["body"]

	tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)

	filename = 'weight_files/logreg_tfidf.sav'
	# load the model from disk
	loaded_model = pickle.load(open(filename, 'rb'))
	prediction=loaded_model.predict([X_test])
	# print ('-----',prediction, idx_flair[prediction[0]])
	return idx_flair[prediction[0]], str(posts['flair'])

