from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="specify name of the video", required=True)
video_put_args.add_argument("views", type=int, help="specify views for video", required=True)
video_put_args.add_argument("likes", type=int, help="specify likes for video", required=True)

videos = {}

def if_no_video(video_id):
    if video_id not in videos:
        abort(404, message='video not found')

def if_video(video_id):
    if video_id in videos:
        abort(400, message='video already exists')

class Video(Resource):
    def get(self, video_id):
        if_no_video(video_id)
        return  videos[video_id]

    def put(self, video_id):
        if_video(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        if_no_video(video_id)
        del videos[video_id]
        return '', 204

api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

