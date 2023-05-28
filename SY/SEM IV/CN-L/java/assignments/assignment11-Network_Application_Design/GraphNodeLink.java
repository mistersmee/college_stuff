import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Node {
    private String name;
    private List<Link> links;

    public Node(String name) {
        this.name = name;
        this.links = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public void addLink(Node node, int weight) {
        links.add(new Link(node, weight));
    }

    public List<Link> getLinks() {
        return links;
    }
}

class Link {
    private Node node;
    private int weight;

    public Link(Node node, int weight) {
        this.node = node;
        this.weight = weight;
    }

    public Node getNode() {
        return node;
    }

    public int getWeight() {
        return weight;
    }
}

class Graph {
    private Map<String, Node> nodes;

    public Graph() {
        this.nodes = new HashMap<>();
    }

    public void addNode(String name) {
        nodes.put(name, new Node(name));
    }

    public void addLink(String from, String to, int weight) {
        Node fromNode = nodes.get(from);
        Node toNode = nodes.get(to);

        if (fromNode != null && toNode != null) {
            fromNode.addLink(toNode, weight);
        }
    }

    public Node getNode(String name) {
        return nodes.get(name);
    }

    public List<Node> getAllNodes() {
        return new ArrayList<>(nodes.values());
    }
}

public class GraphNodeLink {
    public static void main(String[] args) {
        // Create a graph
        Graph graph = new Graph();

        // Add nodes
        graph.addNode("A");
        graph.addNode("B");
        graph.addNode("C");

        // Add links
        graph.addLink("A", "B", 1);
        graph.addLink("B", "C", 1);
        graph.addLink("A", "C", 3);

        // Print the graph
        List<Node> nodes = graph.getAllNodes();
        for (Node node : nodes) {
            System.out.println("Node: " + node.getName());
            List<Link> links = node.getLinks();
            for (Link link : links) {
                System.out.println("  Link: " + node.getName() + " --> " + link.getNode().getName() + " (Weight: " + link.getWeight() + ")");
            }
        }
    }
}
