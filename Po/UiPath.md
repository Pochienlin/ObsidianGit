# UiPath
UID: 202205191528
Tags: #🌱 
Links: [[Robotics Process Automation]]

-----
# Related articles
1. [[UiPath Packages]]
2. [[UiPath Shortcuts]]
3. [[UiPath Studio Panels for Debugging]]
4. [[UiPath Practices]]

##  Installation
UiPath Learning offers its partner organizations the opportunity to use the UiPath Studio software at no charge through a dedicated Learning license, which is free to students and educators alike, for teaching, learning, and research. 
- The license entitles the user to access UiPath Studio and UiPath StudioX, the automation development software application, along with the UiPath Development Robot to allow for testing and execution of the automation. 
- The Academic Alliance Edition of UiPath Studio is a locked version of the software aligned to the current Studio course resources provided by the UiPath Academic Alliance Partners and UiPath Learning Partners. Moreover, the current UiPath Certified Professional exams are based on this version. 
- One license key allows for the activation of the UiPath Studio software on 2 different machines.
- The license type granted is Named User, to be applied solely to User Mode installs. Instructions for activating the Academic Alliance Edition license will be provided accordingly. 
- Each Academic Alliance Edition license expires after 365 days upon its activation, and it is subject to being extended as long as the Academic Alliance partnership is maintained. 

Using the Academic Alliance Edition ensures that you have the appropriate software version installed which aligns with the curricula and hands-on lab materials. This will avoid any disruptions to your learning experience. This will also ensure that projects can be shared between students and educators without software version differences. If you have installed UiPath Studio Community Edition previously, please uninstall it first before installing the UiPath Studio Academic Alliance Edition. Failure to do this may result in both editions of the software not working correctly. 

If you have previous versions of the Academic Alliance Edition (19.4 or 19.10), please install the new one above it (i.e. no need to uninstall). 

Steps to download and install UiPath Studio Academic Alliance Edition 

Step 1: To download your free copy of the UiPath Studio software, [open the URL](https://www.uipath.com/landing/academic-studio-download). It is a private form designated only for the students and educators who are affiliated with the UiPath Academic Alliance & UiPath Learning Partner institutions. 

Step 2: Fill in your contact details and choose the institution name

Step 3: Click Request Academic Alliance Edition. 
Then, check your email in a couple of minutes. You will receive a link to download the software by email. The email you receive contains the installation guide, the link to download the UiPathStudio.msi file along your dedicated license key. **Make sure you follow the steps in the email and carefully follow this guide.**

The file will begin downloading. Click to open the UiPathStudio.msi once it is downloaded. 

Step 4: Click on the Install button right beside Studio. 

Step 5: Accept the terms in the License Agreement and click on Install. 

Step 6: The software will begin its installation. 

Step 7: Click Finish. If “Launch UiPath Studio” was checked, then UiPath Studio is launched. If not, you can search in your Windows explorer for UiPath Studio to open it. 

Step 8: In the “Welcome to UiPath Studio” window, click on More Options and then Standalone Options to activate your dedicated Academic Alliance Edition of Studio with your license key. 

Step 9: The UiPath Registration window is displayed 
	a. Enter the License Key you received by email, including the dashes. 
	b. Select Automatic activation, but ensure you have an internet connection. 
	c. Click Continue. 
	Your UiPath license is now activated. 
	
Step 10: Now, you can start using UiPath Studio and StudioX software to create automation workflows. 

Step 11: You can switch between the two profiles (Studio or StudioX) at any time by going to Settings – License and Profile – View or Change Profile. 
Choose whether you want to use UiPath Studio or StudioX.

# Version Control

**Overview of Version Control Systems** Version control, also known as source control, is the practice of tracking and managing changes to software code. Version control systems are software tools that help software teams manage changes to source code over time. As development environments have accelerated, version control systems help software teams work faster and smarter. They are especially useful for DevOps teams since they help them to reduce development time and increase successful deployments. Version control software keeps track of every modification to the code in a special kind of database. If a mistake is made, developers can turn back the clock and compare earlier versions of the code to help fix the mistake while minimizing disruption to all team members.

#### **Managing Projects with GIT** 
GIT is a distributed version-control system for tracking changes in source code during software development. In simple words, GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere. All you need to get started with GitHub is an internet connection and a GitHub account which is free. You don’t need to know how to code, use the command line, or install Git In UiPath Studio, switch to the Teams tab and you will find the GIT panel with the following options.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/42vvs3W_QNCr77N1v9DQOA_ced1e14d68e14921aa2437c4d880d3a1_Picture1.png?expiry=1653436800000&hmac=o2OtFzRPq0qFu9tlt528GphrG_kynfulmzwMWK7ebhg)

Here, the options are: 
- Clone Repository: Clone a remote GIT repository. 
- Copy to GIT: Copy the current project to an existing GIT repository. 
- GIT Init: Add the current project to a new local GIT repository. The repository location can be the same as the project folder or a parent folder. 
- Disconnect: Disconnect current project from source control. 
- Change Signature: Used to change commit signature.

#### **Adding a project to GIT** 
GIT Init feature adds the current project to a local GIT repository. To add a project 
- Create or open a project in Studio. Click the Start tab > Team > GIT Init

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/BnqDR54pTC-6g0eeKXwvKA_0b9fa927c0ac4d4ba21197f6bbd9c5a1_Picture-2.png?expiry=1653436800000&hmac=kcRTh6lYfv0nAjjDoVLfqO1C16kcr2f4zSChW9soiZE)

- Select the path to initialize the repository 
- In the Commit Changes window, select project files to add to repository 
- Click the Commit and Push button to commit changes & push to the remote repository 
- To copy the current project to existing GIT repository, use the Copy to GIT button 
- To disconnect from GIT, use the Disconnect option to remove the subversion tag 
For more details, visit: [https://docs.uipath.com/studio/v2020.10/docs/managing-projects-git](https://docs.uipath.com/studio/v2020.10/docs/managing-projects-git "Managing Projects")

#### **Cloning a Remote GIT Repository** 
- In the Team tab, select Clone Repository. The Clone a remote GIT repository window is displayed.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/4TDolNtbTCyw6JTbWzwsmA_e3722db5add54839ba75e81f42d4f9a1_Picture-3.png?expiry=1653436800000&hmac=vlJd_bfuxAyMTk_WR_BfAESGBYP_51AfncX193lYWyo)
- Pick from Clone with HTTPS or Use SSH. 
- Type in the Repository URL and choose an empty Check out directory. 
- Click the Use Credentials or Use Key checkbox to add your Git username or Private Key Path, and password. 
- Click Open, Studio opens the project in the Designer panel. 
- In the Open window, select a project.json file to open in Studio.

#### **Copying project to GIT** 
- Team tab > Copy to GIT
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/00p-JRsoTOuKfiUbKNzreg_3337e2cf599749a1b3381e15e4b545a1_Picture-4.png?expiry=1653436800000&hmac=C3AKOXJErLCLAtmKyeRxU93ge6nyCZIYryxV7fdZfCQ)
• Pick the existing GIT repository folder • Select Yes in Copy to GIT message box

### **Managing Projects with TFS** 
Team Foundation Server (TFS) is the source code management established by Microsoft, used for the project and release management. Team Foundation Server (Microsoft TFS) helps manage teams and their code because TFS offers a combo of version control, issue tracking, and application lifecycle management. 

Here, the options are: 
- Open from TFS: Open a project from a TFS repository. It contains two blocks: Team Project Collection & Team Project. 
- Add to TFS: Add current project to TFS source control. 
- Disconnect: Disconnect current project from source control. 
- Manage TFS Online: Go to the web management interface. 


#### **Setting up TFS in Studio:** 
- Team tab > Open from TFS/ Add to TFS

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/sRPlIRAQRTWT5SEQEDU1eg_6b658d3de1784c1783e2a553452b77a1_Picture-5.png?expiry=1653436800000&hmac=e68MK-ib5kh9nnmp6z1hqj59_0ejLr6AMzkTPToNroA)
• Click Servers in Connect to Azure DevOps Server window • Click Add in Add/Remove Azure DevOps Server window • Fill repository details

#### **Opening a Project from TFS:** • Team tab > Open from TFS
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/2AnslLNKTciJ7JSzSg3Iug_82ca8c3e95ef4505b138fa90bf024fa1_Picture-6.png?expiry=1653436800000&hmac=pGvvs7eh4p9WHCBXR4v1VbfOiN_9tl3uhWd6TvHgwIg)
• Pick server to access from the drop-down menu under the Select a Team Foundation Server (in Connect to Azure DevOps Server window) • Pick team project collection & team project > Connect • Pick a Check out directory

#### **Adding a Project to TFS** 
- Create/open project. Click Start > Team > Add to TFS button
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/WVNWV2udQweTVldrneMHVw_7327d9779bd746898997be0e606a66a1_Picture-7.png?expiry=1653436800000&hmac=_PwUzccjfswJ2zcvSYAeBDeuxGptdWVZytaXT-IOYHA)
• Pick Server to access, team project collection & team project in Connect to Azure DevOps Server window > Connect • Provide path in Remote subfolder > Select .xaml file > Pick Check out directory > Add • In the Check in Changes window, select files to check in > Click Check In

**Editing & Checking in changes in TFS** 
- Connect the project to the TFS repository 
- Select Check Out for Edit for a .xaml file 
- Select Check In for the file. Check In window displays 
- Review changes, check Show Unversioned Files box 
- Click Check In. The latest version is now available in the repository. 
- Click Start > Team > Disconnect
For more details, refer: [https://docs.uipath.com/studio/v2020.10/docs/managing-projects-tfs](https://docs.uipath.com/studio/v2020.10/docs/managing-projects-tfs "Managing Project TFS")

### **Managing Projects with SVN** 
Subversion is used for maintaining current and historical versions of projects. Subversion is an open source centralized version control system. It's licensed under Apache. It's also referred to as a software version and revisioning control system. Here, the options are: 
- Open from SVN: Open a project from an SVN repository. 
- Add to SVN: Add current project to SVN source control. 
- Disconnect: Disconnect current project from source control. 
#### **Opening a project from SVN:** 
- Team tab > Open from SVN to access Open from SVN Repository window
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/xNexy-jaTguXscvo2q4L6w_43df7c001c6e47d988bc41bade749aa1_Picture-8.png?expiry=1653436800000&hmac=gOEx9DLuVx5pc0thc9KaTrG5Gw8uQ-7AB8ZDBY2ghS4)
 - Open repository browser, select a file to open. 
 - Pick empty Check Out directory, fill Username & Password in Use credentials box. Click Ok. 

 The project is now available in the check out directory. 
 
 - Pull main.xaml file from the repository by choosing from two options 
 - Check out latest and edit: opens the latest version of the Main.xaml file from the repository, in edit mode. 
 - Open local as read only

#### **Adding a Project to SVN:** 
- Create/open project. Click Start > Team > Add to SVN button
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8iQ2x0gGTd-kNsdIBq3fNg_42ea992df90447b09568af469e0a6aa1_Picture-9.png?expiry=1653436800000&hmac=E_RWuKxdjp7DXi370AvNPuz42kPjCFWD15h1weTTuPQ)
 - Open repository browser, select a file to open. 
 - Pick empty Check Out directory, fill Username & Password in Use credentials box > Click Add 
 - In the Check in Changes window, select files to add to repository > Click Check In. 
 
 The files are now available in the repository 
 
 #### **Editing & Checking in changes in SVN:** 
 - Connect project to SVN repository 
 - Select Check Out for Edit for an .xaml file 
 - Select Check In for the file. Check In window displays • Review changes, check Show Unversioned Files box 
 - Click Check In 
 - Click Start > Team > Disconnect 
For more details, refer: [https://docs.uipath.com/studio/v2020.10/docs/managing-projects-svn](https://docs.uipath.com/studio/v2020.10/docs/managing-projects-svn "Managing Projects SVN")

#### **Context Menu for TFS & SVN** 
Once a connection with a TFS or SVN repository has been established, you can access the project files via a project panel, that offers the following context menu options:
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/o_btUqMNT3K27VKjDY9ygg_0eb9c93ecad742fe999b89ab0eec6ca1_Screenshot-2021-09-01-145543.png?expiry=1653436800000&hmac=-lCpSCGM1CUU41aknd89k_QAR1Z_G_DQoNInLU8xBfQ)
