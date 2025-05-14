import java.util.logging.Logger;

public class Main {
    private static final Logger logger = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        MP3Player mp3Player = new MP3Player();
        WAVPlayer wavPlayer = new WAVPlayer();

        AudioAdapter audioAdapter = new AudioAdapter(mp3Player, wavPlayer);

        mp3Player.play("audio.mp3");
        wavPlayer.play("audio.wav");

        logger.info("\n--- Usando Adaptador ---");
        audioAdapter.play("audio.mp3");  // MP3 a WAV
        audioAdapter.play("audio.wav");  // WAV a MP3
    }
}
