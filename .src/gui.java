//import javax.swing.*;
//import java.awt.*;
//import java.awt.event.*;
import javax.swing.JButton;  
import javax.swing.JFrame;  
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;
import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.ZonedDateTime;
import java.awt.Image;
import java.time.ZonedDateTime;
import java.time.ZoneId;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class GUI {
    public static void main(String[] args) {  
        // create toplevel container
        JFrame frame=new JFrame();  
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   // close window handler
        frame.setSize(750,480);                                 // set framesize
        //frame.setLayout(null); 

        //////////////// Layout ////////////////
        // |pnl Database actions|
        //   |lbl Database actions|
        //     |btn add item to database|
        //     |btn update items in database|
        //     |btn add code and product name|
        // |pnl Stickers actions|
        //   |lbl Stickers actions|
        //     |btn CCV stickers from .csv file|
        //     |btn BOL stickers from .xls file|
        //     |btn PostNL stickers from .csv file|
        ///////////////////////////////////////////

        // variables
        String suiteLogFile = new String(".bin/suite.log");
        int yLocation = 0;
        int xLocation = 0;
        int colWidth  = 250;
        int secondCol = 300;
        
        int btnHeight = 25;
        int labHeight = 50;
        int txtHeight = 0;


        // create panel
        JPanel pnl1 = new JPanel();
        frame.add(pnl1);

        // create stickers label
        JLabel lab_database = new JLabel("Database actions:");
        frame.add(lab_database);
        lab_database.setBounds(xLocation, yLocation, colWidth, labHeight);
        yLocation+=labHeight;
               
        // create button DBadd
        JButton btn_DBadd = new JButton("Add item to Database");
        frame.add(btn_DBadd);                    // add button to frame
        btn_DBadd.addActionListener(new LaunchDBadd());
        btn_DBadd.setBounds(xLocation, yLocation, colWidth ,btnHeight);      // (x,y,w,h) w.r.t. top left
        yLocation+=btnHeight;
        
        // create button DBmod
        JButton btn_DBmod = new JButton("Modify item in Database");
        frame.add(btn_DBmod);
        btn_DBmod.addActionListener(new LaunchDBmod());
        btn_DBmod.setBounds(xLocation, yLocation, colWidth ,btnHeight);
        yLocation+=btnHeight;

        // create button DBmap
        JButton btn_DBmap = new JButton("Add code-name mapping");
        frame.add(btn_DBmap);
        btn_DBmap.addActionListener(new LaunchDBmap());
        btn_DBmap.setBounds(xLocation, yLocation, colWidth ,btnHeight);
        yLocation+=btnHeight;

        // create button DBmap
        JButton btn_DBanalysis = new JButton("Database Analysis");
        frame.add(btn_DBanalysis);
        btn_DBanalysis.setEnabled(false);
        btn_DBanalysis.addActionListener(new LaunchDBanalysis());
        btn_DBanalysis.setBounds(xLocation, yLocation, colWidth ,btnHeight);
        yLocation+=btnHeight;

        // create stickers label
        JLabel lab_stickers = new JLabel("Stickers actions:");
        frame.add(lab_stickers);
        lab_stickers.setBounds(xLocation, yLocation, colWidth, labHeight);
        yLocation+=labHeight;
               
        // create button CCV
        JButton btn_CCV = new JButton("CCV stickers from .csv file");
        frame.add(btn_CCV);                    // add button to frame
        btn_CCV.setEnabled(true);
        btn_CCV.addActionListener(new LaunchPostColumns());
        btn_CCV.setBounds(xLocation, yLocation, colWidth ,btnHeight);      // (x,y,w,h) w.r.t. top left
        yLocation+=btnHeight;

        // create button BOL order list and labels
        JButton btn_BOL_pick = new JButton("BOL order list and labels from .xls file");
        frame.add(btn_BOL_pick);
        btn_BOL_pick.setEnabled(true);
        btn_BOL_pick.addActionListener(new LaunchOrderListLabels());
        btn_BOL_pick.setBounds(xLocation, yLocation, colWidth ,btnHeight);
        yLocation+=btnHeight;

        // create button BOL
        JButton btn_BOL = new JButton("BOL stickers from .xml file");
        frame.add(btn_BOL);
        btn_BOL.setEnabled(true);
        btn_BOL.addActionListener(new LaunchSelectOrders());
        btn_BOL.setBounds(xLocation, yLocation, colWidth ,btnHeight);
        yLocation+=btnHeight;

        // create button PostNL
        JButton btn_PostNL = new JButton("PostNL stickers from .csv file");
        frame.add(btn_PostNL);
        btn_PostNL.setEnabled(false);
        btn_PostNL.addActionListener(new LaunchDBmap());
        btn_PostNL.setBounds(xLocation, yLocation, colWidth ,btnHeight);
        yLocation+=btnHeight;

        // create file conversion label
        JLabel lab_conversion = new JLabel("File Conversion:");
        frame.add(lab_conversion);
        lab_conversion.setBounds(xLocation, yLocation, colWidth, labHeight);
        yLocation+=labHeight;

        // button MisterMinit file conversion
        JButton btn_MM = new JButton("MisterMinit file conversion");
        frame.add(btn_MM);
        btn_MM.setEnabled(true);
        btn_MM.addActionListener(new LaunchMMconversion());
        btn_MM.setBounds(xLocation, yLocation, colWidth ,btnHeight);
        yLocation+=btnHeight;        

        /*// create png image
        ImageIcon img1 = new ImageIcon(new ImageIcon(".bin/statsgraph.png").getImage().getScaledInstance(270, 270, Image.SCALE_DEFAULT));
        JLabel lab_img = new JLabel(img1);
        frame.add(lab_img);
        lab_img.setBounds(400, 500, 270, 270);*/

        xLocation+=colWidth;                // second column
        txtHeight=yLocation-2*btnHeight;    // determine the height of the text area at this point.
        yLocation=0;                        // set yloc back to 0

        // logging label
        JLabel lab_logging = new JLabel("Logging:");
        frame.add(lab_logging);
        lab_logging.setBounds(xLocation, yLocation, colWidth, labHeight);    
        yLocation+=labHeight; 

        // text log field
        JTextArea textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        frame.add(scrollPane);
        //textArea.addActionListener();
        scrollPane.setBounds(xLocation, yLocation, 2*colWidth, txtHeight);

        xLocation+=colWidth;                // third column
        yLocation=0;                        // set yloc back to 0

        // clear log button
        JButton btn7 = new JButton("Clear log");
        frame.add(btn7);
        btn7.setEnabled(true);
        btn7.addActionListener(ev -> {
            try {
                // backup and remove logfile
                ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
                String[] cmd1 = {"mv", suiteLogFile, suiteLogFile+".org"};
                String[] cmd2 = {"touch", suiteLogFile};
                Process p1 = Runtime.getRuntime().exec(cmd1);
                p1.waitFor();
                Process p2 = Runtime.getRuntime().exec(cmd2);
                p2.waitFor();
                System.out.println(now + ": Cleared logfile.");
                // clear pane
                ZonedDateTime now2 = ZonedDateTime.now(ZoneId.systemDefault());
                BufferedReader input = new BufferedReader(new InputStreamReader(new FileInputStream(suiteLogFile)));
                textArea.read(input, "READING FILE");
                System.out.println(now2 + ": Refreshed logfile pane.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }); 
        btn7.setBounds(xLocation, yLocation, colWidth, btnHeight);
        yLocation+=btnHeight;

        // update button
        JButton btn8 = new JButton("Update log");
        frame.add(btn8);
        btn8.setEnabled(true);
        btn8.addActionListener(ev -> {
            try {
                ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
                BufferedReader input = new BufferedReader(new InputStreamReader(new FileInputStream(suiteLogFile)));
                textArea.read(input, "READING FILE");
                System.out.println(now + ": Requested logfile update.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }); 
        btn8.setBounds(xLocation, yLocation, colWidth, btnHeight);
        yLocation+=btnHeight;
    
        frame.setLayout(null);    

        /*// start virtual environment -> SKIP ("source" does not work for java)
        ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
        try {
            System.out.println(now + ": starting virtual environment.");
            //create process and execute
            String[] cmd = { "source", ".venv/bin/activate"};
            Process p = Runtime.getRuntime().exec(cmd);
        } catch (Exception ex) {
            ex.printStackTrace();
        }*/
        
    }

    /*// fileviewer code
    static class FileViewer implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                BufferedReader input = new BufferedReader(new InputStreamReader(new FileInputStream("suite.log")));
                //textArea.read(input, "READING FILE");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }*/
    
    // create new class for button action LaunchDBadd
    static class LaunchDBadd implements ActionListener{
        public void actionPerformed (ActionEvent e){
            ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
            try {
                //create process and execute
                String[] cmd = { "python3", ".src/StoreBase.py", "DBadd" };
                Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": Add item to database.");
                /*p.waitFor();
                ZonedDateTime now2 = ZonedDateTime.now(ZoneId.systemDefault());
                BufferedReader input = new BufferedReader(new InputStreamReader(new FileInputStream(suiteLogFile)));
                textArea.read(input, "READING FILE");
                System.out.println(now2 + ": Refreshed logfile pane.");*/
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }
    
    // create new class for button action LaunchDBmod
    static class LaunchDBmod implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
                String[] cmd = { "python3", ".src/StoreBase.py", "DBmod" };
                Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": Modify item in database.");
                /*p.waitFor();
                ZonedDateTime now2 = ZonedDateTime.now(ZoneId.systemDefault());
                BufferedReader input = new BufferedReader(new InputStreamReader(new FileInputStream(suiteLogFile)));
                textArea.read(input, "READING FILE");
                System.out.println(now2 + ": Refreshed logfile pane.");*/
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }
    
    // create new class for button action LaunchDBmap
    static class LaunchDBmap implements ActionListener{
        public void actionPerformed (ActionEvent e){
            ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
            try {
                String[] cmd = { "python3", ".src/StoreBase.py", "DBmap" };
                Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": Add code-name mapping.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

    // create new class for button action LaunchDBmap
    static class LaunchPostColumns implements ActionListener{
        public void actionPerformed (ActionEvent e){
            ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
            try {
                String[] cmd = { "python3", ".src/PostColumns.py" };
                Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": CCV stickers from .csv file.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

    // create new class for button action LaunchDBmap
    static class LaunchOrderListLabels implements ActionListener{
        public void actionPerformed (ActionEvent e){
            ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
            try {
                String[] cmd = { "python3", ".src/BOL_Picklijst.py" };
                Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": BOL oder list and labels from .xls file.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

    // create new class for button action LaunchDBmap
    static class LaunchSelectOrders implements ActionListener{
        public void actionPerformed (ActionEvent e){
            ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
            try {
                String[] cmd = { "python3", ".src/PostColumns.py" };
                Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": BOL stickers from .xml file.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

    // create new class for button action LaunchMMconversion
    static class LaunchMMconversion implements ActionListener{
        public void actionPerformed (ActionEvent e){
            ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
            try {
                String[] cmd = { "python3", ".src/MMconversion.py" };
                Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": MisterMinit file conversion.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

    // create new class for button action LaunchDBanalysis
    static class LaunchDBanalysis implements ActionListener{
        public void actionPerformed (ActionEvent e){
            ZonedDateTime now = ZonedDateTime.now(ZoneId.systemDefault());
            try {
                //String[] cmd = { "python3", ".src/MMconversion.py" };
                //Process p = Runtime.getRuntime().exec(cmd);
                System.out.println(now + ": Database Analysis.");
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

}