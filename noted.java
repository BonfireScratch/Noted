import java.awt.*; 
import javax.swing.*; 
import java.io.*; 
import java.awt.event.*; 
import javax.swing.plaf.metal.*; 
import javax.swing.text.*;

class noted extends JFrame implements ActionListener { 
    JTextArea t; 

    JFrame f; 
   
    noted() 
    { 
        f = new JFrame("Noted"); 
  
        try { 
            UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel"); 
  
            MetalLookAndFeel.setCurrentTheme(new OceanTheme()); 
        } 
        catch (Exception e) { 
        } 
  
        t = new JTextArea(); 
  
        JMenuBar mb = new JMenuBar(); 
  
        JMenu m1 = new JMenu("File"); 
  
        JMenuItem mi1 = new JMenuItem("New"); 
        JMenuItem mi2 = new JMenuItem("Open"); 
        JMenuItem mi3 = new JMenuItem("Save"); 
        JMenuItem mi9 = new JMenuItem("Print"); 
  
        mi1.addActionListener(this); 
        mi2.addActionListener(this); 
        mi3.addActionListener(this); 
        mi9.addActionListener(this); 
  
        m1.add(mi1); 
        m1.add(mi2); 
        m1.add(mi3); 
        m1.add(mi9); 
  
        JMenu m2 = new JMenu("Edit"); 
  
        JMenuItem mi4 = new JMenuItem("Cut"); 
        JMenuItem mi5 = new JMenuItem("Copy"); 
        JMenuItem mi6 = new JMenuItem("Paste"); 
  
        mi4.addActionListener(this); 
        mi5.addActionListener(this); 
        mi6.addActionListener(this); 
  
        m2.add(mi4); 
        m2.add(mi5); 
        m2.add(mi6); 
  
        mb.add(m1); 
        mb.add(m2); 
  
        f.setJMenuBar(mb); 
        f.add(t); 
        f.setSize(500, 500); 
        f.show(); 
    } 
  
    public void actionPerformed(ActionEvent e) 
    { 
        String s = e.getActionCommand(); 
  
        if (s.equals("Cut")) { 
            t.cut(); 
        } 
        else if (s.equals("Copy")) { 
            t.copy(); 
        } 
        else if (s.equals("Paste")) { 
            t.paste(); 
        } 
        else if (s.equals("Save")) { 
            JFileChooser j = new JFileChooser("f:"); 
  
            int r = j.showSaveDialog(null); 
  
            if (r == JFileChooser.APPROVE_OPTION) { 
  
                File fi = new File(j.getSelectedFile().getAbsolutePath()); 
  
                try { 
                    FileWriter wr = new FileWriter(fi, false); 
  
                    BufferedWriter w = new BufferedWriter(wr); 
  
                    w.write(t.getText()); 
  
                    w.flush(); 
                    w.close(); 
                } 
                catch (Exception evt) { 
                    JOptionPane.showMessageDialog(f, evt.getMessage()); 
                } 
            } 
            else
                JOptionPane.showMessageDialog(f, "the user cancelled the operation"); 
        } 
        else if (s.equals("Print")) { 
            try { 
                t.print(); 
            } 
            catch (Exception evt) { 
                JOptionPane.showMessageDialog(f, evt.getMessage()); 
            } 
        } 
        else if (s.equals("Open")) { 
            JFileChooser j = new JFileChooser("f:"); 
  
            int r = j.showOpenDialog(null); 
  
            if (r == JFileChooser.APPROVE_OPTION) { 
                File fi = new File(j.getSelectedFile().getAbsolutePath()); 
  
                try { 
                    String s1 = "", sl = ""; 
  
                    FileReader fr = new FileReader(fi); 
  
                    BufferedReader br = new BufferedReader(fr); 
  
                    sl = br.readLine(); 
  
                    while ((s1 = br.readLine()) != null) { 
                        sl = sl + "\n" + s1; 
                    } 
  
                    t.setText(sl); 
                } 
                catch (Exception evt) { 
                    JOptionPane.showMessageDialog(f, evt.getMessage()); 
                } 
            } 
            else
                JOptionPane.showMessageDialog(f, "the user cancelled the operation"); 
        } 
        else if (s.equals("New")) { 
            t.setText(""); 
        }
    } 
  
    public static void main(String args[]) 
    { 
        noted e = new noted(); 
    } 
} 
