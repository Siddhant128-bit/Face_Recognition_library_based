# Nice Code written from scratch by siddhant sharma  bugs or things to be sorted: Classification of this thing called result_status and on that basis the color change other then that all is pretty fine
import cv2
import face_recognition
import os

i=0
db='DB'
known_faces=[]
known_names=[]
status=[]
FRAME_THICKNESS=1
FONT_THICKNESS=1




#loading images set from the db
for name in os.listdir(db):
    for imgname in os.listdir(f"{db}/{name}/"):
        for img in os.listdir(f"{db}/{name}/{imgname}/"):
            image=face_recognition.load_image_file(f"{db}/{name}/{imgname}/{img}")
            encoding=face_recognition.face_encodings(image)[i]
            ++i
            known_faces.append(encoding)
            print(img)
            known_names.append(imgname)
            status.append(name)

print(status)
print(known_names)


#get a video feed and capture the image
cap = cv2.VideoCapture(0)
while(True):
    face=[]
    identity=[]
    result_name=""
    result_status=""
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite('test.jpg',frame)

    #converting the obtained image to encoding for comparison
    image=face_recognition.load_image_file(f"{'test.jpg'}")
    #image=cv2.cvtColor(unknown_image,cv2.COLOR_RGB2BGR)
    unknown_encoding=face_recognition.face_encodings(image)
    n=len(known_names)
    count=0

    #having individual face encoding laoded from the face
    for c in unknown_encoding:
        #print(c)
        results = face_recognition.compare_faces(known_faces, c)
        N=len(results)
        #print(N)
        #print(results)
        if True in results:
            x=results.index(True)
            print(results)
            print(x)
            result_name=str(known_names[x])
            result_status=str(status[x])
            #for name in os.listdir(db):
            #    for imgname in os.listdir(f"{db}/{name}"):
            #        if imgname==result_name:
            #            result_status=name

            print(result_status)
            #result_name=result_name.replace('.jpg','')
            identity.append(result_name)
            face.append(count)
            count=count+1

        else:
            count=count+1
        print(count)
        n=len(face)
        #print(n)
        for i in range(n):
            locations=face_recognition.face_locations(image,model='hog')
            top_left=(locations[face[i]][3],locations[face[i]][0])
            buttom_right=(locations[face[i]][1],locations[face[i]][2])

        if result_status=='Known':
                #for i in range(n):
                    #locations=face_recognition.face_locations(image,model='hog')
                    #top_left=(locations[face[i]][3],locations[face[i]][0])
                    #buttom_right=(locations[face[i]][1],locations[face[i]][2])
                    color=[0,255,0]
                    cv2.rectangle(frame,top_left,buttom_right,color,FRAME_THICKNESS)
                    top_left=(locations[face[i]][3],locations[face[i]][2])
                    buttom_righ=(locations[face[i]][1],locations[face[i]][2]+22)
                    cv2.rectangle(frame,top_left,buttom_right,color,FRAME_THICKNESS)
                    cv2.rectangle(frame,(locations[face[i]][3],locations[face[i]][2]),(locations[face[i]][3]+128,locations[face[i]][2]+20),color,cv2.FILLED,FRAME_THICKNESS)
                    cv2.putText(frame,'Status:'+result_status,(locations[face[i]][3],locations[face[i]][2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),FONT_THICKNESS)
                    cv2.rectangle(frame,(locations[face[i]][3],locations[face[i]][2]+22),(locations[face[i]][3]+128,locations[face[i]][2]+35),color,cv2.FILLED,FRAME_THICKNESS)
                    cv2.putText(frame,identity[i],(locations[face[i]][3],locations[face[i]][2]+32),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),FONT_THICKNESS)


        elif result_status=='Restricted':
                #for i in range(n):
                    #locations=face_recognition.face_locations(image,model='hog')
                    #top_left=(locations[face[i]][3],locations[face[i]][0])
                    #buttom_right=(locations[face[i]][1],locations[face[i]][2])
                    color=[0,0,255]
                    cv2.rectangle(frame,top_left,buttom_right,color,FRAME_THICKNESS)
                    top_left=(locations[face[i]][3],locations[face[i]][2])
                    buttom_righ=(locations[face[i]][1],locations[face[i]][2]+22)
                    cv2.rectangle(frame,top_left,buttom_right,color,FRAME_THICKNESS)
                    cv2.rectangle(frame,(locations[face[i]][3],locations[face[i]][2]),(locations[face[i]][3]+128,locations[face[i]][2]+20),color,cv2.FILLED,FRAME_THICKNESS)
                    cv2.putText(frame,'Status:'+result_status,(locations[face[i]][3],locations[face[i]][2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),FONT_THICKNESS)
                    cv2.rectangle(frame,(locations[face[i]][3],locations[face[i]][2]+22),(locations[face[i]][3]+128,locations[face[i]][2]+35),color,cv2.FILLED,FRAME_THICKNESS)
                    cv2.putText(frame,identity[i],(locations[face[i]][3],locations[face[i]][2]+32),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),FONT_THICKNESS)



    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
os.remove("test.jpg")
cap.release()
cv2.destroyAllWindows()
