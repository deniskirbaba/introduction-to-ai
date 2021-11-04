import numpy as np
import matplotlib.pyplot as plt
import random
import time
import matplotlib


def cluster_points(X, mu):
	clusters = {}
	for x in X:
		bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]]))
					for i in enumerate(mu)], key=lambda t:t[1])[0]
		try:
			clusters[bestmukey].append(x)
		except KeyError:
			clusters[bestmukey] = [x]
	return clusters


def reevaluate_centers(mu, clusters):
	newmu = []
	keys = sorted(clusters.keys())
	for k in keys:
		newmu.append(np.mean(clusters[k], axis = 0))
	return newmu


def has_converged(mu, oldmu):
	return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))


def find_centers(X, K, ax, fig):
	# Initialize to K random centers
	oldmu = random.sample(X, K)
	mu = random.sample(X, K)
	while not has_converged(mu, oldmu):
		oldmu = mu
		# Assign all points in X to clusters
		clusters = cluster_points(X, mu)
		# Plotting
		plot_clusters(clusters, mu, ax, fig)
		# Reevaluate centers
		mu = reevaluate_centers(oldmu, clusters)
	return(mu, clusters)


def init_board(N):
	X = np.array([(random.uniform(-1, 1)) for i in range(N)])
	return X


def plot_clusters(clusters, mu, ax, fig):
	for k in clusters.keys():
		x = []
		y = []
		for i in clusters[k]:
			x.append(i[0])
			y.append(i[1])
		ax.scatter(x, y)
		#ax.scatter(mu[k-1][0], mu[k-1][1], s=200, marker='*', c='black')
	fig.canvas.flush_events()

def main():

	X = [init_board(5000), init_board(5000)]
	XX = []
	for i in range(5000):
		XX.append(np.array([X[0][i], X[1][i]]))

	matplotlib.use("TkAgg")
	plt.ion()
	fig = plt.figure()
	ax = fig.add_subplot()
	ax.set(xlim=(-1, 1), ylim=(-1,1))
	ax.scatter(X[0], X[1])
	fig.canvas.flush_events()
	time.sleep(1)
	find_centers(XX, 10, ax, fig)
	plt.waitforbuttonpress()


if __name__ == "__main__":
    main()