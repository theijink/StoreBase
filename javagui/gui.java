//import javax.swing.*;
//import java.awt.*;
//import java.awt.event.*;
import javax.swing.JButton;  
import javax.swing.JFrame;  
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUI {
    public static void main(String[] args) {  
        // create toplevel container
        JFrame frame=new JFrame();  
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   // close window handler
        frame.setSize(720,480);                                 // set framesize

        // create panel
        JPanel pnl1 = new JPanel();
        frame.add(pnl1);
                        
        // create button          
        JButton btn1 = new JButton("Add item to Database");
        pnl1.add(btn1);                    // add button to frame
        btn1.addActionListener(new Action());
        //btn1.setBounds(50,50, 150,50);      // (x,y,w,h) w.r.t. top left
        //frame.setLayout(null); 
    }
    
    // create new class for button action
    static class Action implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                //System.out.println("Executing java code")
                //create process and execute
                String[] cmd = { "python3", "pygui/gui.py" };
                Process p = Runtime.getRuntime().exec(cmd);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }       
    }  
}