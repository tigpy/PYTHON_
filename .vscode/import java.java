import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class SearchEngine {

    private static final String DOC_PATTERN = ".*\\.txt";
    private static final String DOC_PATH = "path/to/documents";
    private static final String[] STOPWORDS = { "a", "an", "the", "and", "or", "but", "not", "of", "to", "in", "on", "at", "with", "from", "by", "for" };

    private Map<String, Set<String>> index;

    public SearchEngine() {
        index = new HashMap<>();
    }

    public void indexDocuments(String path) throws IOException {
        File directory = new File(path);
        if (!directory.isDirectory()) {
            throw new IllegalArgumentException("Path is not a directory");
        }
        for (File file : directory.listFiles()) {
            if (file.isFile() && file.getName().matches(DOC_PATTERN)) {
                indexDocument(file);
            }
        }
    }

    private void indexDocument(File file) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] words = preprocessText(line);
                for (String word : words) {
                    if (!index.containsKey(word)) {
                        index.put(word, new HashSet<>());
                    }
                    index.get(word).add(file.getName());
                }
            }
        }
    }

    private String[] preprocessText(String text) {
        String[] words = text.replaceAll("[^a-zA-Z ]", "").toLowerCase().split("\\s+");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            boolean isStopword = false;
            for (String stopword : STOPWORDS) {
                if (word.equals(stopword)) {
                    isStopword = true;
                    break;
                }
            }
            if (!isStopword) {
                result.add(word);
            }
        }
        return result.toArray(new String[result.size()]);
    }

    public Set<String> searchDocuments(String query) {
        String[] words = preprocessText(query);
        Set<String> result = new HashSet<>(index.get(words[0]));
        for (int i = 1; i < words.length; i++) {
            if (index.containsKey(words[i])) {
                result.retainAll(index.get(words[i]));
            } else {
                return new HashSet<>();
            }
        }
        return result;
    }

    public static void main(String[] args) {
        SearchEngine engine = new SearchEngine();
        try {
            engine.indexDocuments(DOC_PATH);
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.print("Enter your query (type \"exit\" to quit): ");
                String query = scanner.nextLine();
                if (query.equals("exit")) {
                    break;
                }
                Set<String> result = engine.searchDocuments(query);
                System.out.println("Results:");
                if (result.isEmpty()) {
                    System.out.println("No documents found");
                } else {
                    for (String doc : result) {
                        System.out.println(doc);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
