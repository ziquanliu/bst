import bst_class
import numpy as np
import pickle
#t=bst_class.bst()
#for i in np.random.rand(50)*100:
#    t.insert(int(i))
#pickle.dump(t,open('bst_tree.pkl','wb'))
t=pickle.load(open('bst_tree.pkl','rb'))
print 'whole tree:'
print t
#print t.find(78).parent
#print 'max:'
#print t.max_t()
#print '\n'
#print 'min:'
#print t.min_t()
#print t.find_suc(79)
#print t.root.right.left.parent
print t.find_pre(54)
